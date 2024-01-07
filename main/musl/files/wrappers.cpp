#include <stdint.h>
#include <stdio.h>
#include <errno.h>

extern "C" {
#include "pthread_impl.h"
}

#include "platform.h"
#include "allocator_config.h"
#include "stats.h"

/* we don't use standard lib so define a placement-new */
inline void *operator new (size_t, void *p) { return p; }
inline void  operator delete (void *, void *) {}

/* we will request 64k memory at a time
 *
 * this may be as little as 1 page on some systems,
 * and it will hold around 8 TSDs
 */
#ifndef MUSL_SCUDO_TSD_CHUNK
#define MUSL_SCUDO_TSD_CHUNK 65536
#endif

/* the secondary cache was not found to be not much of a benefit
 * (typically higher rss and often worse performance) while also
 * causing some strange jank on qemu-user/riscv builders, so drop
 * it at least for now
 */
#ifndef MUSL_SCUDO_USE_SECONDARY_CACHE
#define MUSL_SCUDO_USE_SECONDARY_CACHE 0
#endif

inline constexpr size_t size_round(size_t sz, size_t align) {
    return ((sz + align - 1) / align) * align;
}

template<typename T, typename TM>
inline constexpr size_t tsds_in_chunk() {
    return (MUSL_SCUDO_TSD_CHUNK - sizeof(TM)) / size_round(sizeof(T), alignof(T));
}

/* tsd registry implementation specific to musl pthreads
 *
 * we need to use a custom one, because the existing exclusive registry
 * relies on thread_local for its state initialization and the tsd object
 * itself, which will mess things up for main thread for dynamic executables
 * loaded through ldso, and also uses pthread keys and stuff, which we do
 * not like for libc
 *
 * so map the tsd object memory manually, and keep track of it using a custom
 * algorithm, storing only one pointer to the tsd object within the thread
 * object internally
 *
 * we map chunks of MUSL_SCUDO_TSD_CHUNK size, each containing storage for
 * as many TSD objects as possible (the first chunk is allocated almost
 * immediately, for the fallback TSD); these are managed like a linked list,
 * so that when threads exit, their TSDs are given back to the list to be
 * reused; in case we run out, a new chunk is mapped as needed
 *
 * to make sure that we don't just map memory and never release any, the
 * chunks are freed as necessary; the strategy is that there can only ever
 * be one chunk that is fully empty - that effectively means an empty chunk
 * is unmapped when another chunk becomes empty
 *
 * the 64k value was chosen for the chunk size as it's the maximum size of
 * a single page one is generally to encounter, which means on these systems
 * only a single page will be mapped at a time (on other systems, it will be
 * multiple pages); regardless of page size, the chunk will be able to fit
 * several TSDs
 */

template<typename TSD>
class TSDAllocator {
    struct chunk;

    struct tsdata {
        TSD tsd;
        tsdata *next;
        chunk *parent;
        uint32_t dirty: 1;
        uint32_t unused: 1;
    };

    struct chunk_meta {
        chunk *below;
        chunk *above;
        unsigned short nused;
    };

    struct chunk {
        tsdata tsds[tsds_in_chunk<tsdata, chunk_meta>()];
        chunk_meta m;
    };

    static_assert(sizeof(chunk) < MUSL_SCUDO_TSD_CHUNK, "chunk too large");

    void init_chunk(chunk *ch) {
        ch->m.below = p_chunks;
        ch->m.above = nullptr;
        ch->m.nused = 0;
        if (p_chunks) {
            p_chunks->m.above = ch;
        }
        p_chunks = ch;
        /* init links */
        auto tsdn = (sizeof(ch->tsds) / sizeof(tsdata));
        for (size_t i = 0; i < (tsdn - 1); ++i) {
            ch->tsds[i].parent = ch;
            ch->tsds[i].next = &ch->tsds[i + 1];
            ch->tsds[i].dirty = 0;
            ch->tsds[i].unused = 1;
        }
        ch->tsds[tsdn - 1].parent = ch;
        ch->tsds[tsdn - 1].next = nullptr;
        ch->tsds[tsdn - 1].dirty = 0;
        ch->tsds[tsdn - 1].unused = 1;
        /* init unused */
        p_unused = ch->tsds;
    }

    void release_freechunk() {
        if (!p_freechunk) {
            return;
        }
        /* unmap and unset whatever previous freechunk we may have
         *
         * doing this ensures that whenever there may be a newly
         * gained empty chunk, the previous empty chunk will be
         * unmapped, so there is always at most one and never more
         */
        auto *ch = p_freechunk;
        p_freechunk = nullptr;
        /* update chunks pointer if needed */
        if (ch == p_chunks) {
            p_chunks = ch->m.below;
        }
        /* first unchain */
        if (ch->m.below) {
            ch->m.below->m.above = ch->m.above;
        }
        if (ch->m.above) {
            ch->m.above->m.below = ch->m.below;
        }
        /* decide based on where our first pointer was positioned */
        auto *sp = p_unused;
        if (sp->parent == ch) {
            /* we were at the beginning */
            while (sp->parent == ch) {
                sp = sp->next;
            }
            p_unused = sp;
        } else {
            /* we were in the middle or at the end */
            while (sp->next->parent != ch) {
                sp = sp->next;
            }
            auto *ep = sp->next;
            while (ep && (ep->parent == ch)) {
                ep = ep->next;
            }
            sp->next = ep;
        }
        /* then unmap */
        scudo::unmap(ch, sizeof(chunk));
    }

    tsdata *p_unused = nullptr;
    chunk *p_chunks = nullptr;
    chunk *p_freechunk = nullptr;

public:
    TSD *request() {
        if (!p_unused) {
            auto *ch = static_cast<chunk *>(scudo::map(
                nullptr, sizeof(chunk), "scudo:tsdchunk"
            ));
            new (ch) chunk{};
            init_chunk(ch);
        } else if (p_unused->parent == p_freechunk) {
            /* chunk will be occupied again */
            p_freechunk = nullptr;
        }
        /* yoink */
        tsdata *tsd = p_unused;
        p_unused = p_unused->next;
        tsd->next = nullptr;
        tsd->unused = 0;
        ++tsd->parent->m.nused;
        /* wipe dirty (recycled) tsds first */
        if (tsd->dirty) {
            memset(&tsd->tsd, 0, sizeof(tsd->tsd));
            new (&tsd->tsd) TSD{};
        }
        return &tsd->tsd;
    }

    /* return it to the allocator; the TSD is destroyed but tsdata is not */
    void release(TSD *tsd) {
        tsdata *p;
        /* get original structure */
        memcpy(&p, &tsd, sizeof(void *));
        /* get parent chunk */
        auto *ch = p->parent;
        /* empty chunk? */
        if (!--ch->m.nused) {
            /* drop the previous freechunk if needed */
            release_freechunk();
            /* assign new freechunk once empty */
            p_freechunk = ch;
        }
        /* delay memset until it's actually needed */
        p->dirty = 1;
        /* try to locate a unused node */
        for (size_t i = 0; i < (sizeof(ch->tsds) / sizeof(tsdata)); ++i) {
            if (ch->tsds[i].unused) {
                auto *pp = &ch->tsds[i];
                auto *pn = pp->next;
                pp->next = p;
                p->next = pn;
                p->unused = 1;
                /* we are done here */
                return;
            }
        }
        /* couldn't locate a unused node, put it in the front */
        p->unused = 1;
        p->next = p_unused;
        p_unused = p;
    }
};

template<typename A>
struct TSDRegistry {
    using tsd_t = scudo::TSD<A>;

    void enable() {
        atomic_store(&p_disabled, 0U, scudo::memory_order_release);
        p_fallback->unlock();
        p_mtx.unlock();
    }

    void disable() {
        p_mtx.lock();
        p_fallback->lock();
        atomic_store(&p_disabled, 1U, scudo::memory_order_release);
    }

    /* this is normally adjustable through setOption, but we do not have
     * mallopt, which means setOption is never actually called by anything
     * (and does not exist for this registry) so return the sane default
     */
    bool getDisableMemInit() { return false; }

    void getStats(scudo::ScopedString *str) {
        str->append("Iterating each TSD is not supported\n");
    }

    void drainCaches(A *inst) {
        auto *self = get_self();
        inst->drainCache(static_cast<tsd_t *>(self->scudo_tsd));
        p_fallback->lock();
        inst->drainCache(p_fallback);
        p_fallback->unlock();
    }

    void initOnceMaybe(A *inst) {
        scudo::ScopedLock L{p_mtx};
        init_once_maybe(inst);
    }

    ALWAYS_INLINE void initThreadMaybe(A *inst, bool minimal) {
        auto *self = get_self();
        if (LIKELY(self->scudo_tsd)) {
            return;
        }
        init_thread(inst, self);
    }

    ALWAYS_INLINE tsd_t *getTSDAndLock(bool *unlock) {
        auto *self = get_self();
        if (LIKELY(
            self->scudo_tsd &&
            !scudo::atomic_load(&p_disabled, scudo::memory_order_acquire)
        )) {
            *unlock = false;
            return static_cast<tsd_t *>(self->scudo_tsd);
        }
        p_fallback->lock();
        *unlock = true;
        return p_fallback;
    }

private:
    friend void ::__malloc_tsd_teardown(void *p);

    /* return it to the allocator */
    void dispose(A *inst, tsd_t *tsd) {
        /* commit back and destroy, no need to lock yet */
        tsd->commitBack(inst);
        tsd->~tsd_t();
        {
            scudo::ScopedLock L{p_mtx};
            p_talloc.release(tsd);
        }
    }

    /* assumes locked p_mtx */
    void init_once_maybe(A *inst) {
        if (LIKELY(p_init)) {
            return;
        }
        inst->init();
        p_fallback = p_talloc.request();
        p_fallback->init(inst);
        p_init = true;
    }

    void init_thread(A *inst, struct pthread *self) {
        tsd_t *tsd;
        {
            scudo::ScopedLock L{p_mtx};
            init_once_maybe(inst);
            tsd = p_talloc.request();
        }
        tsd->init(inst);
        self->scudo_tsd = tsd;
        inst->callPostInitCallback();
    }

    static struct pthread *get_self() {
        struct pthread *p;
        pthread_t s = __pthread_self();
        memcpy(&p, &s, sizeof(struct pthread *));
        return p;
    }

    bool p_init = false;
    scudo::atomic_u8 p_disabled = {};
    tsd_t *p_fallback = nullptr;
    TSDAllocator<tsd_t> p_talloc;
    scudo::HybridMutex p_mtx;
};

using Origin = scudo::Chunk::Origin;

struct MuslConfig {
    static const bool MaySupportMemoryTagging = true;

    template<typename A>
    using TSDRegistryT = TSDRegistry<A>;

    /* we are not actually using primary64 at the moment, as primary32
     * appears to have similar performance and memory usage even on
     * 64-bit systems, while mapping far less virtual memory, which
     * entirely eliminates our qemu performance issues besides other
     * things; maybe reevaluate another time
     */
    struct Primary {
        /* use table-driven size classes, found to perform better */
        using SizeClassMap = scudo::AndroidSizeClassMap;

#if 0 /*SCUDO_WORDSIZE == 64U*/
        /* use pointer compacting like android, improves memory use */
        using CompactPtrT = uint32_t;

        /* too large values result in large mmaps (which will result in terrible
         * performance in qemu-user, for example), too small values may result
         * in size class exhaustion; for now use the same value as android
         */
        static const uintptr_t RegionSizeLog = 28U;
        static const uintptr_t GroupSizeLog = 20U;
        static const uintptr_t CompactPtrScale = SCUDO_MIN_ALIGNMENT_LOG;
        static const uintptr_t MapSizeIncrement = 1UL << 18;
        static const bool EnableRandomOffset = true;
#else
        using CompactPtrT = uintptr_t;

        static const uintptr_t RegionSizeLog = FIRST_32_SECOND_64(18U, 20U);
        static const uintptr_t GroupSizeLog = FIRST_32_SECOND_64(18U, 20U);
#endif
        static const int32_t MinReleaseToOsIntervalMs = INT32_MIN;
        static const int32_t MaxReleaseToOsIntervalMs = INT32_MAX;
    };
#if 0 /*SCUDO_WORDSIZE == 64U*/
    template<typename C> using PrimaryT = scudo::SizeClassAllocator64<C>;
#else
    template<typename C> using PrimaryT = scudo::SizeClassAllocator32<C>;
#endif

#if MUSL_SCUDO_USE_SECONDARY_CACHE
    struct Secondary {
        struct Cache {
            static const uint32_t EntriesArraySize = 32U;
            static const uint32_t QuarantineSize = 0U;
            static const uint32_t DefaultMaxEntriesCount = 32U;
            static const uintptr_t DefaultMaxEntrySize = 1UL << 19;
            static const int32_t MinReleaseToOsIntervalMs = INT32_MIN;
            static const int32_t MaxReleaseToOsIntervalMs = INT32_MAX;
        }
        template<typename C> using CacheT = scudo::MapAllocatorCache<C>;
    };
#else
    struct Secondary {
        template<typename C> using CacheT = scudo::MapAllocatorNoCache<C>;
    };
#endif
    template<typename C> using SecondaryT = scudo::MapAllocator<C>;
};

extern "C" {

extern int __malloc_replaced;
extern int __aligned_alloc_replaced;

static void malloc_postinit();

static SCUDO_REQUIRE_CONSTANT_INITIALIZATION
scudo::Allocator<MuslConfig, malloc_postinit> o_alloc;

#define MALLOC_ALIGN FIRST_32_SECOND_64(8U, 16U)

static void malloc_postinit() {
    o_alloc.initGwpAsan();
}

void __malloc_atfork(int who) {
    if (who < 0) {
        o_alloc.disable();
    } else {
        o_alloc.enable();
    }
}

void __malloc_tsd_teardown(void *p) {
    using T = scudo::TSD<decltype(o_alloc)>;
    auto *tsdp = static_cast<T **>(p);
    auto *tsd = *tsdp;
    if (!tsd) {
        return;
    }
    *tsdp = nullptr;
    o_alloc.getTSDRegistry()->dispose(&o_alloc, tsd);
}

void *__libc_calloc(size_t m, size_t n) {
    if (n && m > (((size_t)-1) / n)) {
        if (o_alloc.canReturnNull()) {
            errno = ENOMEM;
            return nullptr;
        }
        scudo::reportCallocOverflow(m, n);
    }
    auto *ptr = o_alloc.allocate(n * m, Origin::Malloc, MALLOC_ALIGN, true);
    if (UNLIKELY(!ptr)) {
        errno = ENOMEM;
    }
    return ptr;
}

void __libc_free(void *ptr) {
    o_alloc.deallocate(ptr, Origin::Malloc);
}

void *__libc_malloc_impl(size_t len) {
    auto *ptr = o_alloc.allocate(len, Origin::Malloc, MALLOC_ALIGN);
    if (UNLIKELY(!ptr)) {
        errno = ENOMEM;
    }
    return ptr;
}

void *__libc_realloc(void *ptr, size_t len) {
    if (!ptr) {
        auto *ptr = o_alloc.allocate(len, Origin::Malloc, MALLOC_ALIGN);
        if (UNLIKELY(!ptr)) {
            errno = ENOMEM;
        }
        return ptr;
    }
    if (len == 0) {
        o_alloc.deallocate(ptr, Origin::Malloc);
        return nullptr;
    }
    ptr = o_alloc.reallocate(ptr, len, MALLOC_ALIGN);
    if (UNLIKELY(!ptr)) {
        errno = ENOMEM;
    }
    return ptr;
}

/* this has loose checking of align like memalign, but this matches musl's
 * aligned_alloc, which is also used to implement memalign as well as
 * posix_memalign and it allows for replacement of just aligned_alloc,
 * so that is our baseline
 */
INTERFACE void *aligned_alloc(size_t align, size_t len) {
    if (UNLIKELY(!scudo::isPowerOfTwo(align))) {
        if (o_alloc.canReturnNull()) {
            errno = EINVAL;
            return nullptr;
        }
        scudo::reportAlignmentNotPowerOfTwo(align);
    }
    if (UNLIKELY(__malloc_replaced && !__aligned_alloc_replaced)) {
        errno = ENOMEM;
        return nullptr;
    }
    auto *ptr = o_alloc.allocate(len, Origin::Malloc, align);
    if (UNLIKELY(!ptr)) {
        errno = ENOMEM;
    }
    return ptr;
}

INTERFACE size_t malloc_usable_size(void *p) {
    return o_alloc.getUsableSize(p);
}

/* we have no way to implement this AFAICT */
void __malloc_donate(char *, char *) {}

} // extern "C"
