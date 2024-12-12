#!/bin/sh

for kpath in /usr/lib/modules/*; do
    # probably means we did not match anything...
    [ -d "$kpath" ] || continue
    # don't touch kernels that this system does not manage
    [ -f "${kpath}/apk-dist/.apk-series" ] || continue
    # just sanitize further just in case
    [ -f "${kpath}/apk-dist/modules.order" ] || continue
    # if stamped, it's up to date and we can skip it
    [ -f "${kpath}/.apk-stamp" ] && continue
    # extract the version
    kver=${kpath#/usr/lib/modules/}
    # already set up; the kernel changed, so clean it...
    if [ -f "${kpath}/modules.order" ]; then
        # nuke everything in modules.order, those come with the kernel
        for modn in $(cat "${kpath}/modules.order"); do
            rm -f "${kpath}/${modn}"*
        done
        # nuke everything in ckms binary manifests
        for manifd in "${kpath}/ckms-manifest/"*; do
            [ -d "$manifd" ] || continue
            modn=${manifd#${kpath}/ckms-manifest/}
            for manif in "${manifd}/"*; do
                [ -f "$manif" ] || continue
                modv=${manif#${manifd}/}
                # drop the modules
                for modn in $(cat "$manif"); do
                    rm -f "${kpath}/${modn}"*
                done
                # drop disablers
                rm -f "${kpath}/ckms-disable/${modn}/${modv}"
            done
        done
        # drop bootdir
        rm -rf "${kpath}/boot"
        # prune empty dirs
        find "${kpath}" -type d -empty -exec rmdir {} \+
        # and remove module files...
        rm -f "${kpath}"/modules.*
        # remove stamps too if present
        rm -f "${kpath}"/.apk-*
    fi
    echo "Setting up kernel: ${kver}..."
    # setup, hardlink things; use rsync because there may be existing
    # files managed by say, ckms, and we want to merge them without pain
    if ! rsync -a "--link-dest=${kpath}/apk-dist" "${kpath}/apk-dist/" "$kpath"; then
        echo "SETUP FAILED: $kver"
        continue
    fi
    # deal with boot files, use rsync again to let them overlay nicely
    if [ -d "${kpath}/boot" ]; then
        # just in case if there was a dbg package and now there isn't
        [ -f "${kpath}/boot/System.map-${kver}" ] || rm -f "/boot/System.map-${kver}"
        # resync boot files, noop if unchanged
        if ! rsync -a "--link-dest=${kpath}/boot" "${kpath}/boot/" /boot; then
            echo "SETUP FAILED: $kver"
            continue
        fi
    fi
    # update copied stamp
    touch "${kpath}/.apk-stamp"
done

exit 0
