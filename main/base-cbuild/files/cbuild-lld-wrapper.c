/* a replacement driver wrapper for lld so we can control threads
 *
 * this file is a part of Chimera Linux, and provided under
 * the same license as the overall cports tree (BSD-2-Clause)
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <err.h>

int main(int argc, char **argv) {
    FILE *f = fopen("/tmp/cbuild-lld-args", "rb");
    if (!f) {
        goto do_exec;
    }

    fseek(f, 0, SEEK_END);
    long fsz = ftell(f);
    if (fsz < 0) {
        err(1, NULL);
    }
    fseek(f, 0, SEEK_SET);

    if (fsz == 0) {
        fclose(f);
        goto do_exec;
    }

    char *buf = malloc(fsz + 1);
    if (!buf || (fread(buf, 1, fsz, f) < (size_t)fsz)) {
        err(1, NULL);
    }
    buf[fsz] = '\0';

    fclose(f);

    /* separate the args */
    size_t eargs = 0;
    char *p = buf, *np;
    for (;;) {
        np = strchr(p, '\n');
        if (!np) {
            if (*p) {
                ++eargs;
            }
            break;
        }
        *np = '\0';
        ++eargs;
        p = np + 1;
    }

    /* space to fit argv + our extra args + a null terminator */
    char **args = malloc((argc + eargs + 1) * sizeof(char *));
    if (!args) {
        err(1, NULL);
    }

    size_t i = 0;
    args[i++] = argv[0];
    /* add extra arguments */
    while (eargs) {
        size_t al = strlen(buf);
        if (al) {
            args[i++] = buf;
        }
        buf += al;
        buf += 1;
        --eargs;
    }
    /* add remaining arguments */
    for (int a = 1; a <= argc; ++a) {
        args[i++] = argv[a];
    }

    argv = args;

do_exec:
    execv("/usr/bin/lld", argv);
    err(1, NULL);
    return 1;
}
