#!/bin/sh

do_depmod() {
    echo "depmod: $1"
    if [ -f /boot/System.map-$1 ]; then
        depmod -a -F /boot/System.map-$1 $1
    else
        depmod -a $1
    fi
}

for kpath in /usr/lib/modules/*; do
    # only consider kernel dirs
    [ -f "${kpath}/modules.order" ] || continue
    # only consider those that haven't been depmoded
    [ -f "${kpath}/modules.dep" ] && continue
    # then run depmod...
    kver=$(basename "$kpath")
    # on successful depmod, nuke initramfs so it gets regen
    if do_depmod "$kver"; then
        rm -f "/boot/initramfs-${kver}.img"
        rm -f "/boot/initrd.img-${kver}"
    else
        echo "ERROR: depmod failed for ${kver}..." >&2
    fi
done

exit 0
