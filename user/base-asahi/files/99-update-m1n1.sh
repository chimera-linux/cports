#!/bin/sh

KERNVER=$(linux-version list|linux-version sort|tail -n1)

# no kernel?
[ -z "$KERNVER" ] && exit 0

echo "Updating m1n1 for ${KERNVER}"

DTBS="/boot/dtbs/dtbs-$KERNVER/apple/t[86]*.dtb" update-m1n1
