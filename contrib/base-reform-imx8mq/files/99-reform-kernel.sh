#!/bin/sh
# generate extlinux.conf for mnt reform

KERNVER=$(linux-version list|linux-version sort|tail -n1)

# no kernel?
[ -z "$KERNVER" ] && exit 0

# cmdline file must exist
[ ! -r /etc/default/reform-cmdline ] && exit 0

CMDLINE=$(head -n1 /etc/default/reform-cmdline)

# if empty, do not generate anything, that's a mechanism
# for those who want to handle this fully manually
[ -z "$CMDLINE" ] && exit 0

echo "Setting up MNT Reform kernel ${KERNVER}..."

mkdir -p /boot/extlinux
cat > /boot/extlinux/extlinux.conf <<EOF
LABEL chimera
KERNEL ../vmlinux-${KERNVER}
FDT ../dtbs/dtbs-${KERNVER}/freescale/imx8mq-mnt-reform2.dtb
APPEND initrd=../initrd.img-${KERNVER} ${CMDLINE}
EOF
