#!/bin/sh
# remove leftover ckms bits for removed kernels + build for new kernels

KRET=0

for kern in /usr/lib/modules/*; do
    [ -d "${kern}" ] || continue
    kernver=${kern#/usr/lib/modules/}
    # likely removed kernel
    if [ ! -f "${kern}/modules.dep" ]; then
        ckms -q -k "${kernver}" status | while read sline; do
            status=${sline#*: }
            # extract info
            minfo=$(echo ${sline%: *}|sed 's/, /,/g')
            modn=$(echo $minfo|cut -d, -f1)
            modv=$(echo $minfo|cut -d, -f2)
            kernv=$(echo $minfo|cut -d, -f3)
            if [ "$status" = "installed" ]; then
                ckms -k "${kernv}" uninstall "${modn}=${modv}" || \
                    echo "FAILED: uninstall ${modn}=${modv} for ${kernv}"
            fi
        done || :
        # skip
        continue
    fi
    # existing kernel
    ckms -q -k "${kernver}" status | while read sline; do
        status=${sline#*: }
        # extract info
        minfo=$(echo ${sline%: *}|sed 's/, /,/g')
        modn=$(echo $minfo|cut -d, -f1)
        modv=$(echo $minfo|cut -d, -f2)
        kernv=$(echo $minfo|cut -d, -f3)
        # only added; build it
        if [ "$status" = "added" ]; then
            ckms -k "${kernv}" build "${modn}=${modv}" || \
                echo "FAILED: build ${modn}=${modv} for ${kernv}"
            status="built"
        fi
        # only built; install it
        if [ "$status" = "built" ]; then
            ckms -k "${kernv}" install "${modn}=${modv}" || \
                echo "FAILED: install ${modn}=${modv} for ${kernv}"
        fi
    done || :
done

exit $KRET
