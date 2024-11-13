#!/bin/sh

CONFIG=$1

if [ -z "$CONFIG" ]; then
    CONFIG="/boot/extlinux/extlinux.conf"
fi

U_BOOT_CFG=/etc/default/u-boot
# overridable defaults
U_BOOT_CMDLINE_FILE=/etc/default/u-boot-cmdline
U_BOOT_FDT_FILE=/etc/default/u-boot-fdt
U_BOOT_FDTDIR_FILE=/etc/default/u-boot-fdtdir
U_BOOT_TIMEOUT=3
U_BOOT_MENU_TITLE="Chimera Linux"
U_BOOT_OS_TITLE="Chimera Linux"
U_BOOT_DISABLE_RECOVERY=
U_BOOT_DISABLE_FDT=

# source global config if present
[ -r $U_BOOT_CFG ] && . $U_BOOT_CFG

DEV_CMDLINE=$U_BOOT_CMDLINE
DEV_CMDLINE_DEFAULT=$U_BOOT_CMDLINE_DEFAULT
DEV_EXTRA_CMDLINE=
DEV_FDT=$U_BOOT_FDT
DEV_FDTDIR=$U_BOOT_FDTDIR

if [ -r "$U_BOOT_CMDLINE_FILE" ]; then
    DEV_EXTRA_CMDLINE=$(cat "$U_BOOT_CMDLINE_FILE")
fi

if [ -r "$U_BOOT_FDT_FILE" -a -z "$DEV_FDT" ]; then
    DEV_FDT=$(cat "$U_BOOT_FDT_FILE")
fi

if [ -r "$U_BOOT_FDTDIR_FILE" -a -z "$DEV_FDTDIR" ]; then
    DEV_FDTDIR=$(cat "$U_BOOT_FDTDIR_FILE")
fi

# silently remove old
if [ "$CONFIG" != "-" ]; then
    rm -f "$CONFIG" > /dev/null 2>&1
    echo "Generating U-Boot menu at $CONFIG..."
fi

COUT=$(mktemp)

write_cfg() {
    echo "$@" >> "$COUT"
}

write_fdt() {
    # don't write if dsiabled
    [ -n "$U_BOOT_DISABLE_FDT" ] && return 0
    # first try writing out FDT, if that's enough we leave it there
    case "$2" in
        '') ;;
        /*)
            write_cfg "    FDT $2"
            return 0
            ;;
        *)
            write_cfg "    FDT ../dtbs/dtbs-$1/$2"
            return 0
            ;;
    esac
    # the default implicit behavior is to set FDTDIR to kernel's dtbs dir
    if [ -z "$3" ]; then
        write_cfg "    FDTDIR ../dtbs/dtbs-$1"
        return 0
    fi
    # else write out the fdtdir that is requested
    case "$3" in
        /*)
            write_cfg "    FDTDIR $3"
            ;;
        *)
            write_cfg "    FDTDIR ../dtbs/dtbs-$1/$3"
            ;;
    esac
}

build_cmdline() {
    if [ -f "/boot/initrd.img-$1" ]; then
        printf "initrd=../initrd.img-%s " "$1"
    fi
    if [ -z "$2" ]; then
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
    if [ -n "$2" -a -n "$DEV_CMDLINE_DEFAULT" ]; then
        printf "%s " "$DEV_CMDLINE_DEFAULT"
    fi
}

gen_cmdline() {
    CMDL=$(build_cmdline "$@" | sed 's/[ ]*$//')
    /usr/lib/base-kernel/kernel-root-detect "$CMDL"
}

write_cfg "TIMEOUT $U_BOOT_TIMEOUT"
write_cfg "DEFAULT default"
write_cfg "MENU TITLE $U_BOOT_MENU_TITLE"
write_cfg

GOT_DEFAULT=

for KVER in $(linux-version list | linux-version sort --reverse); do
    # get the actual kernel name
    for KPATH in /boot/vmlinu[xz]-${KVER}; do
        KPATH=$(basename "$KPATH")
        break
    done
    if [ -z "$GOT_DEFAULT" ]; then
        write_cfg "LABEL default"
    else
        write_cfg
        write_cfg "LABEL ${KVER}"
    fi
    write_cfg "    MENU LABEL $U_BOOT_OS_TITLE ($KVER)"
    write_cfg "    KERNEL ../${KPATH}"
    write_fdt "$KVER" "$DEV_FDT" "$DEV_FDTDIR"
    write_cfg "    APPEND $(gen_cmdline ${KVER} 1)"
    if [ -z "$U_BOOT_DISABLE_RECOVERY" ]; then
        write_cfg
        if [ -z "$GOT_DEFAULT" ]; then
            write_cfg "LABEL recovery"
        else
            write_cfg "LABEL ${KVER}_recovery"
        fi
        write_cfg "    MENU LABEL $U_BOOT_OS_TITLE ($KVER, recovery)"
        write_cfg "    KERNEL ../${KPATH}"
        write_fdt "$KVER" "$DEV_FDT" "$DEV_FDTDIR"
        write_cfg "    APPEND $(gen_cmdline ${KVER})"
    fi
    GOT_DEFAULT=1
done

if [ "$CONFIG" = "-" ]; then
    cat "$COUT"
    rm -f "$COUT"
else
    DIRN=$(dirname "$CONFIG")
    mkdir -p "$DIRN"
    mv "$COUT" "$CONFIG"
fi
