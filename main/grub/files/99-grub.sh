#!/bin/sh
# regenerate grub configuration file

if [ ! -d /boot/grub ]; then
    exit 0
fi

ZPOOL_VDEV_NAME_PATH=YES update-grub || :
