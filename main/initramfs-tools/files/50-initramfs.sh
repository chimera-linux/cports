#!/bin/sh
# regenerate initramfs as needed

KRET=0

for KVER in $(linux-version list | linux-version sort --reverse); do
    [ -f "/boot/initrd.img-${KVER}" ] && continue
    update-initramfs -c -k "${KVER}" || KRET=$?
done

exit $KRET
