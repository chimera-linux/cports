#!/bin/sh
# adapted from the void kernel hook
# it's pretty messy so TODO: rewrite

KERNVER=$(linux-version list|linux-version sort|tail -n1)

# no kernel?
[ -z "$KERNVER" ] && exit 0

echo "Setting up Pinebook Pro kernel ${KERNVER}..."

cat > /boot/boot.txt <<EOF
# MAC address (use spaces instead of colons)
setenv macaddr da 19 c8 7a 6d f4
part uuid \${devtype} \${devnum}:\${bootpart} uuid
setenv bootargs console=ttyS2,115200 console=tty1 root=PARTLABEL=root rootwait video=eDP-1:1920x1080@60 loglevel=4
setenv fdtfile rockchip/rk3399-pinebook-pro.dtb
if load \${devtype} \${devnum}:\${bootpart} \${kernel_addr_r} vmlinux-${KERNVER}; then
  if load \${devtype} \${devnum}:\${bootpart} \${fdt_addr_r} dtbs/dtbs-${KERNVER}/\${fdtfile}; then
    fdt addr \${fdt_addr_r}
    fdt resize
    fdt set /ethernet@fe300000 local-mac-address "[\${macaddr}]"
    if load \${devtype} \${devnum}:\${bootpart} \${ramdisk_addr_r} initrd.img-${KERNVER}.img; then
      booti \${kernel_addr_r} \${ramdisk_addr_r}:\${filesize} \${fdt_addr_r};
    else
      booti \${kernel_addr_r} - \${fdt_addr_r};
    fi;
  fi;
fi
EOF

exec mkimage -A arm -O linux -T script -C none -n "U-Boot boot script" -d /boot/boot.txt /boot/boot.scr
