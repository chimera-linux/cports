/* libnvcompat: extra wrapper around libgcompat to provide stuff that is
 * very specific to the nvidia driver; all symbols here start with __nvcompat
 * and are patchelf'd into the nvidia ELFs by doing dynamic symbol remapping
 */

#include <pthread.h>
#include <time.h>

/* RECURSIVE MUTEX INITIALIZERS
 *
 * nvidia uses PTHREAD_RECURSIVE_MUTEX_INITIALIZER_NP to statically init
 * recursive mutexes; musl does not support a static initializer for this
 * which leads to lockups due to some mutexes no longer being considered
 * recursive
 *
 * glibc uses a kind field in the mutex structure for this, which corresponds
 * to __i[4] on 64-bit and __i[3] on 32-bit in musl's mutex layout; musl
 * itself does not currently use this field
 *
 * the actual mutex type is stored in __i[0]; what we do is patch mutex locks
 * in a way that updates the type field upon first lock attempt
 */

/* the kind is only ever written by a static initializer */
#if __SIZE_WIDTH__ == 64
#define m_kind __u.__i[4]
#else
#define m_kind __u.__i[3]
#endif

#define m_type __u.__i[0]

/* we call this before every lock attempt; this means we are making every lock
 * not expensive by a single acquire load, but nothing much better we can do
 *
 * the m_type is read non-atomically by musl (and here), but we make sure any
 * races end up harmless (see comments) while kind is never used by anything
 * so we can treat it atomically as a sort of acquire-release "lock"
 */
static inline void patch_mutex_kind(pthread_mutex_t *m) {
    /* test static kind initializer; test only the kinds */
    int k = __atomic_load_n(&m->m_kind, __ATOMIC_ACQUIRE) & 3;
    /* - k == 0 means it's a regular mutex; bail
     * - k == 3 means it's an adaptive mutex; bail because mutex doesn't have it
     *   but do clear the kind in the mutex structure
     * - m_type being set may mean:
     *  - pthread_mutex_init was called before the lock attempt, which makes
     *    this not a statically initialized mutex and we can bail
     *  - the below store has happened and we can bail
     */
    if (!k || m->m_type) return;
    /* no store */
    if (k == 3) goto release;
    /* update the type; this may technically race and happen multiple times,
     * but we don't care how many times we store, the important part is that
     * kind does not get cleared before this relaxed store, if we do make it
     * here, it means we had a non-zero kind in this call and it's okay
     */
    __atomic_store_n(&m->m_type, k, __ATOMIC_RELAXED);
release:
    /* clear the kind */
    __atomic_store_n(&m->m_kind, 0, __ATOMIC_RELEASE);
}

int __nvcompat_mutex_lock(pthread_mutex_t *m) {
    patch_mutex_kind(m);
    return pthread_mutex_lock(m);
}

int __nvcompat_mutex_timedlock(pthread_mutex_t *restrict m, const struct timespec *restrict at) {
    patch_mutex_kind(m);
    return pthread_mutex_timedlock(m, at);
}

int __nvcompat_mutex_trylock(pthread_mutex_t *m) {
    patch_mutex_kind(m);
    return pthread_mutex_trylock(m);
}
