/* a lightweight cc wrapper that takes care to ignore
 * linker/include path args would otherwise break cross compilation
 *
 * this file is a part of Chimera Linux, and provided under
 * the same license as the overall cports tree (BSD-2-Clause)
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>
#include <unistd.h>
#include <errno.h>

int main(int argc, char **argv) {
    char abuf[PATH_MAX];

    for (int i = 1; i < argc; ++i) {
        const char *ignpath = "/usr/lib";
        if (strncmp(argv[i], "-L", 2)) {
            /* not a linker or include search path arg */
            if (strncmp(argv[i], "-I", 2)) {
                continue;
            } else {
                ignpath = "/usr/include";
            }
        }
        const char *apath = argv[i] + 2;
        int nskip = 1;
        if (!*apath) {
            /* provided as a separate argument */
            apath = argv[i + 1];
            ++nskip;
        }
        char *rp = realpath(apath, abuf);
        if (!rp) {
            /* does not resolve, pass verbatim */
            continue;
        }
        if (!strcmp(rp, ignpath)) {
            /* skip */
            printf("ignoring search path: %s\n", argv[i]);
            argc -= nskip;
            /* shift all args afterwards back */
            memmove(&argv[i], &argv[i + nskip], sizeof(char *) * (argc - i));
            /* we repeat from here again, so unincrement i */
            --i;
            continue;
        }
    }

    /* when called by path, only use the command name */
    const char *ls = strrchr(argv[0], '/');
    if (!ls++) {
        ls = argv[0];
    }

    /* re-terminate if needed */
    argv[argc] = NULL;

    snprintf(abuf, sizeof(abuf), "/usr/bin/%s", ls);

    /* generally this should not return */
    execv(abuf, argv);

    fprintf(stderr, "failed to invoke '%s': %s\n", abuf, strerror(errno));
    return 1;
}
