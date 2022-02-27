#!/bin/sh

# prune modules that are no longer installed

for mod in /var/lib/ckms/*; do
    [ -d "$mod" ] || continue
    for ver in "${mod}"/*; do
        [ -d "${ver}" ] || continue
        # if the module is invalid, just kill it
        if [ ! -f "${ver}/ckms.ini" ]; then
            rm -rf "${ver}"
            continue
        fi
        # otherwise check if still installed
        [ -d "${ver}/source" ] && continue
        # found a missing module; uninstall for every kernel
        for kern in /usr/lib/modules/*; do
            [ -d "${kern}" ] || continue
            ckms -q -k "${kern#/usr/lib/modules/}" uninstall "${ver}" || :
        done
        # purge its state
        rm -rf "${ver}"
    done
done

# add new modules

for mod in /usr/src/*; do
    [ -d "${mod}" ] || continue
    [ -f "${mod}/ckms.ini" ] || continue
    ckms -q add "${mod}" > /dev/null 2>&1 || :
done

# build and install whatever is left

for kern in /usr/lib/modules/*; do
    [ -d "${kern}" ] || continue
    kernver=${kern#/usr/lib/modules/}
    # skip early
    if [ ! -d "${kern}/build" ]; then
        echo "kernel headers not installed for ${kernver}, skipping..."
        continue
    fi
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
