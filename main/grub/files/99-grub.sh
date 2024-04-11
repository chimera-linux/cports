#!/bin/sh
# regenerate grub configuration file

[ -f /etc/default/grub ] && . /etc/default/grub

[ "$GRUB_DISABLE_KERNEL_HOOK" != "true" ] || exit 0
[ -d /boot/grub ] || exit 0

ZPOOL_VDEV_NAME_PATH=YES update-grub || :
