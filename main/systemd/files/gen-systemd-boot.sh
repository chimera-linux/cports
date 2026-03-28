#!/bin/sh

BOOTCTL_CMD=$(command -v bootctl 2>/dev/null)

if [ ! -x "$BOOTCTL_CMD" ]; then
    exit 69
fi

[ -r /etc/os-release ] && . /etc/os-release

SD_BOOT_SYSTEM_CFG=/usr/lib/systemd/boot/systemd-boot
SD_BOOT_CFG=/etc/default/systemd-boot
# overridable defaults
SD_BOOT_SYSTEM_RELAX_ESP_FILE=/usr/lib/systemd/boot/relax-esp
SD_BOOT_SYSTEM_CMDLINE_FILE=/usr/lib/systemd/boot/cmdline
SD_BOOT_SYSTEM_DEVICETREE_FILE=/usr/lib/systemd/boot/devicetree
SD_BOOT_CMDLINE_FILE=/etc/default/systemd-boot-cmdline
SD_BOOT_DEVICETREE_FILE=/etc/default/systemd-boot-devicetree
SD_BOOT_OS_TITLE="$PRETTY_NAME"
SD_BOOT_DISABLE_RECOVERY=
SD_BOOT_ESP_PATH=
SD_BOOT_BOOT_PATH=
SD_BOOT_ENTRY_TOKEN=
SD_BOOT_COUNT_TRIES=
SD_BOOT_DISABLE_DEVICETREE=

[ -z "$SD_BOOT_OS_TITLE" ] && SD_BOOT_OS_TITLE="Chimera Linux"
[ -r /etc/kernel/entry-token ] && SD_BOOT_ENTRY_TOKEN=$(cat /etc/kernel/entry-token)
[ -z "$SD_BOOT_ENTRY_TOKEN" ] && SD_BOOT_ENTRY_TOKEN="chimera"
[ -r /etc/kernel/tries ] && SD_BOOT_COUNT_TRIES=$(cat /etc/kernel/tries)

# source global config if present
[ -r $SD_BOOT_SYSTEM_CFG ] && . $SD_BOOT_SYSTEM_CFG
[ -r $SD_BOOT_CFG ] && . $SD_BOOT_CFG

DEV_CMDLINE=$SD_BOOT_CMDLINE
DEV_CMDLINE_DEFAULT=$SD_BOOT_CMDLINE_DEFAULT
DEV_EXTRA_CMDLINE=
DEV_DEVICETREE=$SD_BOOT_DEVICETREE

if [ -r "$SD_BOOT_CMDLINE_FILE" ]; then
    DEV_EXTRA_CMDLINE=$(cat "$SD_BOOT_CMDLINE_FILE")
elif [ -r "$SD_BOOT_SYSTEM_CMDLINE_FILE" ]; then
    DEV_EXTRA_CMDLINE=$(cat "$SD_BOOT_SYSTEM_CMDLINE_FILE")
fi

if [ -z "$DEV_DEVICETREE" ]; then
    if [ -r "$SD_BOOT_DEVICETREE_FILE" ]; then
        DEV_DEVICETREE=$(cat "$SD_BOOT_DEVICETREE_FILE")
    elif [ -r "$SD_BOOT_SYSTEM_DEVICETREE_FILE" ]; then
        DEV_DEVICETREE=$(cat "$SD_BOOT_SYSTEM_DEVICETREE_FILE")
    fi
fi

if [ -n "$SD_BOOT_RELAX_ESP_CHECKS" ]; then
    export SYSTEMD_RELAX_ESP_CHECKS=1
fi

if [ -e "$SD_BOOT_SYSTEM_RELAX_ESP_FILE" ]; then
    export SYSTEMD_RELAX_ESP_CHECKS=1
fi

if [ -z "$SD_BOOT_ESP_PATH" ]; then
    SD_BOOT_ESP_PATH=$("$BOOTCTL_CMD" -p)
fi
if [ -z "$SD_BOOT_BOOT_PATH" ]; then
    SD_BOOT_BOOT_PATH=$("$BOOTCTL_CMD" -x)
fi

# args override whatever autodetection or config
if [ -n "$1" ]; then
    SD_BOOT_ESP_PATH="$1"
fi
if [ -n "$2" ]; then
    SD_BOOT_BOOT_PATH="$2"
fi

# disabled?
if [ -n "$SD_BOOT_DISABLE_KERNEL_HOOK" ]; then
    exit 1
fi

# not installed?
INSTALLED=$("$BOOTCTL_CMD" "--esp-path=$SD_BOOT_ESP_PATH" "--boot-path=$SD_BOOT_BOOT_PATH" is-installed 2>/dev/null)

if [ "$INSTALLED" != "yes" ]; then
    exit 1
fi

# no paths? exit with unsupported
if ! mountpoint -q "$SD_BOOT_ESP_PATH"; then
    echo "The ESP is not a mount point." >&2
    exit 2
fi
if ! mountpoint -q "$SD_BOOT_BOOT_PATH"; then
    echo "The /boot directory is not a mount point." >&2
    exit 2
fi

# verify if we have block devices for boot as well as esp
ESP_DEV=$(findmnt -no SOURCE "$SD_BOOT_ESP_PATH")
BOOT_DEV=$(findmnt -no SOURCE "$SD_BOOT_BOOT_PATH")

if [ ! -b "$ESP_DEV" -o ! -b "$BOOT_DEV" ]; then
    echo "Could not determine ESP or /boot devices." >&2
    exit 3
fi

if [ "$SYSTEMD_RELAX_ESP_CHECKS" != "1" ]; then
    # make sure ESP is really an ESP
    ESP_PTTYPE=$(lsblk -no PARTTYPE "$ESP_DEV")

    if [ "$ESP_PTTYPE" != "c12a7328-f81f-11d2-ba4b-00a0c93ec93b" ]; then
        echo "The ESP is not an ESP." >&2
        exit 4
    fi

    # make sure ESP is FAT32
    ESP_FSTYPE=$(lsblk -no FSTYPE "$ESP_DEV")

    if [ "$ESP_FSTYPE" != "vfat" ]; then
        echo "The ESP is not FAT32." >&2
        exit 5
    fi
fi

# /boot must be XBOOTLDR when separate
if [ "$ESP_DEV" != "$BOOT_DEV" ]; then
    BOOT_PTTYPE=$(lsblk -no PARTTYPE "$BOOT_DEV")

    if [ "$BOOT_PTTYPE" != "bc13c2ff-59e6-4262-a352-b275fd6f7172" ]; then
        echo "The /boot partition is not Linux extended boot." >&2
        exit 6
    fi
fi

COUTD=$(mktemp -d)

write_cfg() {
    OUTF="${COUTD}/$1"
    shift
    echo "$@" >> "$OUTF"
}

write_devicetree() {
    # do not write if explicitly disabled
    [ -n "$SD_BOOT_DISABLE_DEVICETREE" ] && return 0
    # we don't have dtbdir, so this is best we can do
    case "$2" in
        '') ;;
        /*)
            write_cfg "$CONF_NAME" "devicetree $2"
            ;;
        *)
            write_cfg "$CONF_NAME" "devicetree /dtbs/dtbs-$1/$2"
            ;;
    esac
}

build_cmdline() {
    if [ -z "$1" ]; then
        printf "ro single "
    else
        printf "ro "
    fi
    if [ -n "$DEV_EXTRA_CMDLINE" ]; then
        printf "%s " "$DEV_EXTRA_CMDLINE"
    fi
    if [ -n "$DEV_CMDLINE" ]; then
        printf "%s " "$DEV_CMDLINE"
    fi
    if [ -n "$1" -a -n "$DEV_CMDLINE_DEFAULT" ]; then
        printf "%s " "$DEV_CMDLINE_DEFAULT"
    fi
}

gen_cmdline() {
    CMDL=$(build_cmdline "$@" | sed 's/[ ]*$//')
    /usr/lib/base-kernel/kernel-root-detect "$CMDL"
}

CMDLINE_MULTI=$(gen_cmdline 1)
CMDLINE_SINGLE=$(gen_cmdline)

echo "Generating boot entries for ${SD_BOOT_ENTRY_TOKEN}..."

write_entry() {
    # TODO: respect tries left from pre-existing entries
    if [ -n "$SD_BOOT_COUNT_TRIES" ]; then
        CONF_NAME="${SD_BOOT_ENTRY_TOKEN}-${1}+${SD_BOOT_COUNT_TRIES}.conf"
    else
        CONF_NAME="${SD_BOOT_ENTRY_TOKEN}-${1}.conf"
    fi
    write_cfg "$CONF_NAME" "title ${SD_BOOT_OS_TITLE}"
    write_cfg "$CONF_NAME" "linux /${3}"
    if [ -f "/boot/initrd.img-${2}" ]; then
        write_cfg "$CONF_NAME" "initrd /initrd.img-${2}"
    fi
    write_devicetree "$2" "$DEV_DEVICETREE"
    write_cfg "$CONF_NAME" "options ${4}"
}

for KVER in $(linux-version list | linux-version sort --reverse); do
    # get the actual kernel name
    for KPATH in /boot/vmlinu[xz]-${KVER}; do
        KPATH=$(basename "$KPATH")
        break
    done
    echo "Found kernel: /boot/${KPATH}"
    write_entry "$KVER" "$KVER" "$KPATH" "$CMDLINE_MULTI"
    if [ -z "$SD_BOOT_DISABLE_RECOVERY" ]; then
        write_entry "${KVER}-recovery" "$KVER" "$KPATH" "$CMDLINE_SINGLE"
    fi
done

mkdir -p "${SD_BOOT_BOOT_PATH}/loader/entries"

for f in "${SD_BOOT_BOOT_PATH}/loader/entries/${SD_BOOT_ENTRY_TOKEN}-"*.conf; do
    [ -f "$f" ] && rm -f "$f"
done

mv "${COUTD}/${SD_BOOT_ENTRY_TOKEN}-"*.conf "${SD_BOOT_BOOT_PATH}/loader/entries"
rm -rf "${COUTD}"

exit 0
