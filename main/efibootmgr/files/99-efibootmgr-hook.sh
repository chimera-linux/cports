#!/bin/sh

EFIBOOTMGR_HOOK_CFG=/etc/default/efibootmgr-hook
# overridable defaults
EFIBOOTMGR_ENABLE_HOOK=
EFIBOOTMGR_CMDLINE=
EFIBOOTMGR_CMDLINE_DEFAULT="quiet splash"
EFIBOOTMGR_DISABLE_RECOVERY=
EFIBOOTMGR_ENTRY_TITLE="Chimera Linux"

# source global config if present
[ -r $EFIBOOTMGR_HOOK_CFG ] && . $EFIBOOTMGR_HOOK_CFG

DEV_CMDLINE=$EFIBOOTMGR_CMDLINE
DEV_CMDLINE_DEFAULT=$EFIBOOTMGR_CMDLINE_DEFAULT

# silently quit if disabled
if [ -z "$EFIBOOTMGR_ENABLE_HOOK" ]; then
    exit 0
fi

if [ ! -x "/usr/bin/efibootmgr" ]; then
    echo "ERROR: efibootmgr not found" 1>&2
    exit 1
fi

# /boot must be a mountpoint
BDEV=$(mountpoint -d /boot 2>/dev/null)
if [ $? -ne 0 ]; then
    echo "ERROR: /boot is not a mount point" 1>&2
    exit 1
fi

# map this back to block device
DEVNAME=
. /sys/dev/block/$BDEV/uevent

if [ -z "$DEVNAME" -o -z "$MAJOR" ]; then
    echo "ERROR: could not get /boot device" 1>&2
    exit 1
fi

PARTBLOCK="/dev/$DEVNAME"
PARTTYPE=$(lsblk -n -o PARTTYPE "$PARTBLOCK" 2>/dev/null)

if [ $? -ne 0 ]; then
    echo "ERROR: could not get /boot partition type" 1>&2
    exit 1
fi

PARTTYPE=$(echo "$PARTTYPE" | tr '[:upper:]' '[:lower:]')

if [ "$PARTTYPE" != "c12a7328-f81f-11d2-ba4b-00a0c93ec93b" ]; then
    echo "ERROR: /boot is not an EFI system partition" 1>&2
    exit 1
fi

# partition number of disk
PARTNUM="$PARTN"

# identify the disk itself
DEVNAME=
. /sys/dev/block/$MAJOR:0/uevent

if [ -z "$DEVNAME" -o ! -b "/dev/$DEVNAME" ]; then
    echo "ERROR: could not locate disk for $PARTBLOCK" 1>&2
    exit 1
fi

# located
DISKBLOCK="/dev/$DEVNAME"

# this is mostly it with sanity checks

del_chimeras() {
   for ent in $(/usr/bin/efibootmgr | grep " $EFIBOOTMGR_ENTRY_TITLE " | cut -c "5-8"); do
       /usr/bin/efibootmgr -Bq -b "$ent"
   done
}

add_entry_raw() {
    /usr/bin/efibootmgr -qc -d "$DISKBLOCK" -p "$PARTNUM" -L "$EFIBOOTMGR_ENTRY_TITLE ($1$2)" -l "/$3" -u "$4"
}

add_entry() {
    VMLINUX="vmlinuz-$1"
    [ -f "/boot/$VMLINUX" ] || VMLINUX="vmlinux-$1"
    if [ ! -f "/boot/$VMLINUX" ]; then
        echo "ERROR: could not locate kernel $1"
    fi

    INITRD="initrd.img-$1"
    [ -f "/boot/$INITRD" ] || INITRD="initramfs-$1.img"
    if [ ! -f "/boot/$INITRD" ]; then
        INITRD=
    else
        INITRD="initrd=/$INITRD"
    fi

    CMDLINE="$DEV_CMDLINE"
    CMDLINE_DEFAULT="$DEV_CMDLINE_DEFAULT"
    [ -n "$CMDLINE" ] && CMDLINE=" $CMDLINE"
    [ -n "$CMDLINE_DEFAULT" ] && CMDLINE_DEFAULT=" $CMDLINE_DEFAULT"

    CMDLINE_FULL="ro${CMDLINE}${CMDLINE_DEFAULT}"
    CMDLINE="ro single${CMDLINE}"

    if [ -n "$INITRD" ]; then
        CMDLINE="$CMDLINE $INITRD"
        CMDLINE_FULL="$CMDLINE_FULL $INITRD"
    fi

    CMDLINE_FULL=$(/usr/libexec/base-kernel/kernel-root-detect "$CMDLINE_FULL")
    add_entry_raw "$1" "" "$VMLINUX" "$CMDLINE_FULL"

    if [ -z "$EFIBOOTMGR_DISABLE_RECOVERY" ]; then
        CMDLINE=$(/usr/libexec/base-kernel/kernel-root-detect "$CMDLINE")
        add_entry_raw "$1" ", recovery" "$VMLINUX" "$CMDLINE"
    fi
}

BOOTORDER=$(/usr/bin/efibootmgr | grep "BootOrder: " | cut -c 12-)

# remove old chimera entries first
del_chimeras

for KVER in $(linux-version list | linux-version sort --reverse); do
    add_entry "$KVER"
done

/usr/bin/efibootmgr -qo "$BOOTORDER"

exit 0
