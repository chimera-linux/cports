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

/* tsd registry implementation specific to musl pthreads
 *
 * we need to use a custom one, because the existing exclusive registry
 * relies on thread_local for its state initialization and the tsd object
 * itself, which will mess things up for main thread for dynamic executables
 * loaded through ldso, and also uses pthread keys and stuff, which we do
 * not like for libc
 *
 * so instead implement a very simplified version of the tsd registry that
 * integrates with musl's internals and maps tsd objects on-demand, only
 * storing the pointer within the thread structure
 *
 * we take the approach of mapping (at most) TSD_CHUNK sized chunks, which
 * contain multiple TSDs - this is managed like a linked list, so that when
 * threads exit, their TSDs are given back to the list to be reused; in case
 * we do run out (which happens when there are more concurrently running
 * threads that do allocation than the existing chunks can satisfy), a new
 * one is mapped and linked to the previous.
 *
 * in the end we only map as many chunks as necessary to satisfy the highest
 * number of concurrently running threads in the process; the 64k value was
 * chosen as it's effectively the maximum size of a single page we have on
 * our supported architectures - in those cases, only 1 page will be mapped
 * at a time, but on most systems this will be 16 pages (but always fitting
 * the same number of TSDs regardless)
 */

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

    struct tsdata {
        tsd_t tsd;
        tsdata *next;
    };

    struct chunk {
        tsdata tsds[(MUSL_SCUDO_TSD_CHUNK - sizeof(void *)) / sizeof(tsdata)];
        chunk *next;
    };

    static_assert(sizeof(chunk) < MUSL_SCUDO_TSD_CHUNK, "chunk too large");

    /* chunks are never released, just recycled */
    tsd_t *request() {
        if (!p_unused) {
            auto *ch = static_cast<chunk *>(scudo::map(
                nullptr, sizeof(chunk), "scudo:tsdchunk", 0
            ));
            new (ch) chunk{};
            ch->next = p_chunks;
            p_chunks = ch;
            auto tsdn = (sizeof(ch->tsds) / sizeof(tsdata));
            for (size_t i = 0; i < (tsdn - 1); ++i) {
                ch->tsds[i].next = &ch->tsds[i + 1];
            }
            ch->tsds[tsdn - 1].next = p_unused;
            p_unused = ch->tsds;
        }
        auto *tsd = p_unused;
        p_unused = p_unused->next;
        return &tsd->tsd;
    }

    /* return it to the allocator */
    void dispose(A *inst, tsd_t *tsd) {
        tsdata *p;
        tsd->commitBack(inst);
        tsd->~tsd_t();
        /* zero-fill and reinit */
        memset(tsd, 0, sizeof(*tsd));
        memcpy(&p, &tsd, sizeof(void *));
        new (tsd) tsd_t{};
        {
            scudo::ScopedLock L{p_mtx};
            p->next = p_unused;
            p_unused = p;
        }
    }

    /* assumes locked p_mtx */
    void init_once_maybe(A *inst) {
        if (LIKELY(p_init)) {
            return;
        }
        inst->init();
        p_fallback = request();
        p_fallback->init(inst);
        p_init = true;
    }

    void init_thread(A *inst, struct pthread *self) {
        tsd_t *tsd;
        {
            scudo::ScopedLock L{p_mtx};
            init_once_maybe(inst);
            tsd = request();
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
    tsdata *p_unused = nullptr;
    chunk *p_chunks = nullptr;
    scudo::HybridMutex p_mtx;
};

using Origin = scudo::Chunk::Origin;

struct MuslConfig {
    /* use table-driven size classes, found to perform better */
    using SizeClassMap = scudo::AndroidSizeClassMap;

    static const bool MaySupportMemoryTagging = true;

    /* we are not actually using primary64 at the moment, as primary32
     * appears to have similar performance and memory usage even on
     * 64-bit systems, while mapping far less virtual memory, which
     * entirely eliminates our qemu performance issues besides other
     * things; maybe reevaluate another time
     */
#if 0 /*SCUDO_WORDSIZE == 64U*/
    using Primary = scudo::SizeClassAllocator64<MuslConfig>;
    /* use pointer compacting like android, improves memory use */
    using PrimaryCompactPtrT = uint32_t;

    /* too large values result in large mmaps (which will result in terrible
     * performance in qemu-user, for example), too small values may result
     * in size class exhaustion; for now use the same value as android
     */
    static const uintptr_t PrimaryRegionSizeLog = 28U;
    static const uintptr_t PrimaryCompactPtrScale = SCUDO_MIN_ALIGNMENT_LOG;
    static const uintptr_t PrimaryMapSizeIncrement = 1UL << 18;
    static const bool PrimaryEnableRandomOffset = true;
#else
    using Primary = scudo::SizeClassAllocator32<MuslConfig>;
    using PrimaryCompactPtrT = uintptr_t;

    static const uintptr_t PrimaryRegionSizeLog = FIRST_32_SECOND_64(18U, 20U);
#endif

    static const int32_t PrimaryMinReleaseToOsIntervalMs = INT32_MIN;
    static const int32_t PrimaryMaxReleaseToOsIntervalMs = INT32_MAX;

#if MUSL_SCUDO_USE_SECONDARY_CACHE
    using SecondaryCache = scudo::MapAllocatorCache<MuslConfig>;

    static const uint32_t SecondaryCacheEntriesArraySize = 32U;
    static const uint32_t SecondaryCacheQuarantineSize = 0U;
    static const uint32_t SecondaryCacheDefaultMaxEntriesCount = 32U;
    static const uintptr_t SecondaryCacheDefaultMaxEntrySize = 1UL << 19;
    static const int32_t SecondaryCacheMinReleaseToOsIntervalMs = INT32_MIN;
    static const int32_t SecondaryCacheMaxReleaseToOsIntervalMs = INT32_MAX;
#else
    using SecondaryCache = scudo::MapAllocatorNoCache;
#endif

    template<typename A>
    using TSDRegistryT = TSDRegistry<A>;
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
    auto *reg = o_alloc.getTSDRegistry();
    reg->dispose(&o_alloc, tsd);
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
