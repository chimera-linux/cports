#!/bin/sh
# regenerate initramfs as needed

KRET=0

for f in /boot/vmlinu[xz]-*; do
    KVER=$(echo $f | sed 's/.*vmlinu[xz]-\(.*\)/\1/')
    [ -f "/boot/initrd.img-${KVER}" ] && continue
    update-initramfs -c -k "${KVER}" || KRET=$?
done

exit $KRET
