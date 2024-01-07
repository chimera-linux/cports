#!/bin/sh

DEVICE=$1
ROOT=$2

if [ -z "$DEVICE" ]; then
    echo "Usage: $0 WHOLE_DISK_IN_DEV [ROOT]" >&2
    exit 1
fi

if [ ! -b "$DEVICE" ]; then
    echo "ERROR: the argument must be a block device (whole disk)" >&2
    exit 1
fi

U_BOOT_CFG="${ROOT}/etc/default/u-boot"
U_BOOT_DEVICE_FILE="${ROOT}/etc/default/u-boot-device"
U_BOOT_DEVICE=

[ -r "$U_BOOT_CFG" ] && . "$U_BOOT_CFG"

if [ -z "$U_BOOT_DEVICE" -a -r "$U_BOOT_DEVICE_FILE" ]; then
    U_BOOT_DEVICE=$(cat "$U_BOOT_DEVICE_FILE")
fi

if [ -z "$U_BOOT_DEVICE" ]; then
    echo "ERROR: u-boot device name is not known" >&2
    exit 1
fi

UBPATH="${ROOT}/usr/lib/u-boot/${U_BOOT_DEVICE}"

if [ ! -d "$UBPATH" ]; then
    echo "ERROR: could not locate u-boot for '${U_BOOT_DEVICE}'" >&2
    exit 1
fi

if [ ! -x "${UBPATH}/flash.sh" ]; then
    echo "ERROR: could not locate flasher for '${U_BOOT_DEVICE}'" >&2
    exit 1
fi

exec "${UBPATH}/flash.sh" "$DEVICE" "$UBPATH"
