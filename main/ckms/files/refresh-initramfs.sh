#!/bin/sh
#
# initramfs refresh hook for ckms within chimera

if [ -n "$CKMS_APK_DEFER_INITRAMFS" ]; then
    echo "Deferring initramfs refresh for ${1}..."
    touch "/boot/initrd.img-${1}.ckms-defer"
    exit $?
fi

update-initramfs -u -k "${1}"
