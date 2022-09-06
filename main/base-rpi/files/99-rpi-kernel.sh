#!/bin/sh
# generate kernel.txt for raspberry pi
# and copy over the right overlays and so on

KERNVER=$(linux-version list|linux-version sort|tail -n1)

# no kernel?
[ -z "$KERNVER" ] && exit 0

echo "Setting up Raspberry Pi kernel ${KERNVER}..."

# device tree blobs
rm -f /boot/*.dtb || :
cp /boot/dtbs/dtbs-${KERNVER}/broadcom/*.dtb /boot
# dtoverlays
rm -rf /boot/overlays || :
cp -R /boot/dtbs/dtbs-${KERNVER}/overlays /boot

# generate kernel.txt
rm -f /boot/kernel.txt || :
echo kernel=vmlinux-${KERNVER} >> /boot/kernel.txt
echo initramfs initrd.img-${KERNVER} followkernel >> /boot/kernel.txt
