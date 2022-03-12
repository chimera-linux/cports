#!/bin/sh
# remove leftover ckms bits for removed kernels + build for new kernels

export CKMS_APK_DEFER_INITRAMFS=1

for kern in /usr/lib/modules/*; do
    [ -d "${kern}" ] || continue
    kernver=${kern#/usr/lib/modules/}
    # only consider removed kernels
    [ -f "${kern}/modules.dep" ] || continue
    # uninstall everything installed for that kernel
    ckms -q -k "${kernver}" status | sed 's/[:,]//g' | \
        while read modn modv kernv karch status; do
            # only consider installed modules
            [ "$status" = "installed" ] || continue
            # uninstall
            ckms -k "${kernv}" uninstall "${modn}=${modv}" || \
                echo "FAILED: uninstall ${modn}=${modv} for ${kernv}"
        done || :
done

exec /usr/libexec/ckms-install-all
