#!/bin/sh
#
# initramfs refresh hook for ckms within chimera

if [ -n "$CKMS_APK_DEFER_INITRAMFS" ]; then
    rm -f "/boot/initramfs-${1}.img"
    rm -f "/boot/initrd.img-${1}"
    exit 0
fi

update-initramfs -u -k "${1}"
