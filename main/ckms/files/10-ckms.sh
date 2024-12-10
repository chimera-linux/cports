#!/bin/sh

export CKMS_APK_DEFER_INITRAMFS=1
export CKMS_APK_DEFER_DEPMOD=1

# prune statedirs for system-disabled (binary) modules first
for kern in /usr/lib/modules/*; do
    [ -d "${kern}" ] || continue
    kernver=${kern#/usr/lib/modules/}
    for dismod in "${kern}/ckms-disable"/*; do
        [ -d "${dismod}" ] || continue
        modname=${dismod#${kern}/ckms-disable/}
        for disver in "${dismod}"/*; do
            [ -e "${disver}" ] || continue
            modver=${disver#${dismod}/}
            modbase="/var/lib/ckms/${modname}"
            # nuke kernel-specific state bits
            rm -rf "${modbase}/${modver}/${kernver}"
            rm -f "${modbase}/kernel-${kernver}-"*
        done
    done
done

# clean up whatever ckms manages if the kernel is already gone

for kern in /usr/lib/modules/*; do
    [ -d "${kern}" ] || continue
    kernver=${kern#/usr/lib/modules/}
    # only consider removed kernels
    [ -f "${kern}/modules.order" ] && continue
    # skip early
    [ "${kernver}" = "apk-backup" ] && continue
    # uninstall everything installed for that kernel
    ckms -q -k "${kernver}" plain-status | \
        while read modn modv kernv karch status; do
            # remove installed modules
            if [ "$status" = "installed" ]; then
                # uninstall
                ckms -k "${kernv}" uninstall "${modn}=${modv}" || \
                    echo "FAILED: uninstall ${modn}=${modv} for ${kernv}"
                status="built"
            fi
            if [ "$status" = "built" -o "$status" = "built+disabled" ]; then
                # clean up
                ckms -k "${kernv}" clean "${modn}=${modv}" || \
                    echo "FAILED: clean ${modn}=${modv} for ${kernv}"
            fi
        done || :
done

# after that, prune ckms modules that are no longer installed

for mod in /var/lib/ckms/*; do
    [ -d "$mod" ] || continue
    for ver in "${mod}"/*; do
        # installed-module symlink, skip
        if [ -L "${ver}" ]; then
            # prune if needed though...
            [ -e "${ver}" ] || rm -f "${ver}"
            continue
        fi
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
            kern="${kern#/usr/lib/modules/}"
            [ "${kern}" = "apk-backup" ] && continue
            ckms -q -k "${kern}" uninstall "${ver}" || :
        done
        # purge its state
        rm -rf "${ver}"
    done
done

# finally add whatever new modules

for mod in /usr/src/*; do
    [ -d "${mod}" ] || continue
    [ -f "${mod}/ckms.ini" ] || continue
    ckms -q add "${mod}" > /dev/null 2>&1 || :
done

# and build them...

for kern in /usr/lib/modules/*; do
    [ -d "${kern}" ] || continue
    kernver=${kern#/usr/lib/modules/}
    # possibly not a kernel, or at least not modular
    [ -f "${kern}/modules.order" ] || continue
    # skip early
    if [ ! -d "${kern}/build" ]; then
        echo "kernel headers not installed for ${kernver}, skipping..."
        continue
    fi
    ckms -q -k "${kernver}" plain-status | \
        while read modn modv kernv karch status; do
            # only added; build it
            if [ "$status" = "added" ]; then
                ckms -k "${kernv}" build "${modn}=${modv}"
                if [ $? -ne 0 ]; then
                    echo "FAILED: build ${modn}=${modv} for ${kernv}"
                    continue
                fi
                status="built"
            fi
            # only built; install it
            if [ "$status" = "built" ]; then
                ckms -k "${kernv}" install "${modn}=${modv}"
                if [ $? -ne 0 ]; then
                    echo "FAILED: install ${modn}=${modv} for ${kernv}"
                    continue
                fi
            fi
        done
done

exit 0
