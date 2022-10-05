#!/bin/sh
# generate extlinux.conf for hifive unmatched

KERNVER=$(linux-version list|linux-version sort|tail -n1)

# no kernel?
[ -z "$KERNVER" ] && exit 0

# cmdline file must exist
[ ! -r /etc/default/unmatched-cmdline ] && exit 0

CMDLINE=$(head -n1 /etc/default/unmatched-cmdline)

# if empty, do not generate anything, that's a mechanism
# for those who want to handle this fully manually
[ -z "$CMDLINE" ] && exit 0

echo "Setting up HiFive Unmatched kernel ${KERNVER}..."

mkdir -p /boot/extlinux
cat > /boot/extlinux/extlinux.conf <<EOF
LABEL chimera
KERNEL ../vmlinux-${KERNVER}
FDT ../dtbs/dtbs-${KERNVER}/sifive/hifive-unmatched-a00.dtb
APPEND initrd=../initrd.img-${KERNVER} ${CMDLINE}
EOF
