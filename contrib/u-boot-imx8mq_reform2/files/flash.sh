#!/bin/sh

DEVICE=$1
UBPATH=$2

[ -n "$DEVICE" -a -n "$UBPATH" ] || exit 32
[ -b "$DEVICE" ] || exit 33
[ -r "${UBPATH}/flash.bin" ] || exit 34

dd if="${UBPATH}/flash.bin" of="${DEVICE}" seek=66 conv=notrunc,fsync || exit 35
