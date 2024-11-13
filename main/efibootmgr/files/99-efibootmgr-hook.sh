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

if [ -z "$DEVNAME" -o -z "$MAJOR" -o -z "$MINOR" -o -z "$PARTN" ]; then
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
DISKBLOCK="/dev/${DEVNAME%$PARTNUM}"
DISKBLOCK="${DISKBLOCK%p}"

if [ ! -b "$DISKBLOCK" ]; then
    echo "ERROR: could not locate disk for $PARTBLOCK" 1>&2
    exit 1
fi

# this is mostly it with sanity checks

# old bootorder that should be preserved best we can
# include a leading comma for easier/more robust manipulation
BOOTORDER=,$(/usr/bin/efibootmgr | grep "BootOrder: " | cut -c 12-)
BOOTORDER_GAP=",+"

del_chimeras() {
   for ent in $(/usr/bin/efibootmgr | grep " $EFIBOOTMGR_ENTRY_TITLE " | cut -c "5-8"); do
       /usr/bin/efibootmgr -Bq -b "$ent"
       # mark one gap in bootorder
       BOOTORDER=$(echo "$BOOTORDER" | sed "s/,${ent}/${BOOTORDER_GAP}/")
       BOOTORDER_GAP=
   done
   # if no gap was created, create one at the end
   BOOTORDER="${BOOTORDER}${BOOTORDER_GAP}"
}

order_chimeras() {
    # even if the numbers might not be in the right order, the entries in the list should be
    for ent in $(/usr/bin/efibootmgr | grep " $EFIBOOTMGR_ENTRY_TITLE " | cut -c "5-8"); do
        BOOTORDER=$(echo "$BOOTORDER" | sed "s/,+/,${ent},+/")
    done
    # and drop the gap marker
    BOOTORDER=$(echo "$BOOTORDER" | sed "s/,+//")
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
        INITRD="initrd=\\$INITRD"
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

    CMDLINE_FULL=$(/usr/lib/base-kernel/kernel-root-detect "$CMDLINE_FULL")
    add_entry_raw "$1" "" "$VMLINUX" "$CMDLINE_FULL"

    if [ -z "$EFIBOOTMGR_DISABLE_RECOVERY" ]; then
        CMDLINE=$(/usr/lib/base-kernel/kernel-root-detect "$CMDLINE")
        add_entry_raw "$1" ", recovery" "$VMLINUX" "$CMDLINE"
    fi
}

# remove old chimera entries first
del_chimeras

for KVER in $(linux-version list | linux-version sort --reverse); do
    add_entry "$KVER"
done

# set up correct boot order
order_chimeras

# reset the order but strip the leading comma
/usr/bin/efibootmgr -qo "${BOOTORDER#,}"

exit 0
