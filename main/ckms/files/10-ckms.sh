#!/bin/sh
# remove leftover ckms bits for removed kernels + build for new kernels

KRET=0

export CKMS_APK_DEFER_INITRAMFS=1

for kern in /usr/lib/modules/*; do
    [ -d "${kern}" ] || continue
    kernver=${kern#/usr/lib/modules/}
    # likely removed kernel
    if [ ! -f "${kern}/modules.dep" ]; then
        ckms -q -k "${kernver}" status | sed 's/[:,]//g' | \
            while read modn modv kernv karch status; do
                if [ "$status" = "installed" ]; then
                    ckms -k "${kernv}" uninstall "${modn}=${modv}" || \
                        echo "FAILED: uninstall ${modn}=${modv} for ${kernv}"
                fi
            done || :
        # skip
        continue
    fi
    # existing kernel
    ckms -q -k "${kernver}" status | sed 's/[:,]//g' | \
        while read modn modv kernv karch status; do
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

# deal with deferred initramfs

for f in /boot/initrd.img-*.ckms-defer; do
    [ -f "$f" ] || continue
    kernver=${f#/boot/initrd.img-}
    kernver=${kernver%.ckms-defer}
    update-initramfs -u -k "${kernver}" || \
        echo "FAILED: update-initramfs for ${kernver}"
    rm -f "$f"
done

exit $KRET
