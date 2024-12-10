#!/bin/sh
# regenerate initramfs as needed

KRET=0

for KVER in $(linux-version list | linux-version sort --reverse); do
    if [ ! -f "/boot/initrd.img-${KVER}" ]; then
        # refresh because it does not exist
        update-initramfs -c -k "$KVER" || KRET=$?
    elif [ -n "$KERNEL_D_CHANGE_INITRAMFS_TOOLS" ]; then
        # refresh because hooks changed
        update-initramfs -c -k "$KVER" || KRET=$?
    elif [ -n "$KERNEL_D_CHANGE_FIRMWARE" ]; then
        # refresh because firmware changed
        update-initramfs -c -k "$KVER" || KRET=$?
    fi
    # else do nothing...
done

exit $KRET
