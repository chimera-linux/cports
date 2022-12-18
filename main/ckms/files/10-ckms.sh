#!/bin/sh
# remove leftover ckms bits for removed kernels + build for new kernels

export CKMS_APK_DEFER_INITRAMFS=1

for kern in /usr/lib/modules/*; do
    [ -d "${kern}" ] || continue
    kernver=${kern#/usr/lib/modules/}
    # only consider removed kernels
    [ -f "${kern}/modules.dep" ] && continue
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

exec /usr/libexec/ckms-install-all
