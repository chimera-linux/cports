#!/bin/sh

DEVICE=$1
UBPATH=$2

[ -n "$DEVICE" -a -n "$UBPATH" ] || exit 32
[ -b "$DEVICE" ] || exit 33
[ -r "${UBPATH}/u-boot-spl.bin" ] || exit 34
[ -r "${UBPATH}/u-boot.itb" ] || exit 34

dd if="${UBPATH}/u-boot-spl.bin" of="${DEVICE}" seek=34 conv=notrunc,fsync || exit 35
dd if="${UBPATH}/u-boot.itb" of="${DEVICE}" seek=2082 conv=notrunc,fsync || exit 35
