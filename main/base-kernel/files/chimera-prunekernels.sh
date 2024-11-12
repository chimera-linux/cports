#!/bin/sh
#
# This is a helper script to handle cleanup of backed up Chimera kernels.
#
# Usage:
#
# $ chimera-prunekernels list [version ...]
# $ chimera-prunekernels rm [version ...]
# $ chimera-prunekernels rm all
#
# I (q66 <q66@chimera-linux.org>) hereby place this script in the public domain.
#

PROGNAME=$0

usage() {
        cat << EOF
Usage: $PROGNAME list|rm [version|all ...]
EOF
}

die() {
    echo "ERROR: " $* 1>&2
    exit 1
}

COMMAND=$1

if [ -z "$COMMAND" ]; then
    usage 1>&2
    exit 1
fi

shift

list_kernels_raw() {
    curk=$(uname -r)
    for x in "$@"; do
        for item in /usr/lib/modules/apk-backup/*; do
            [ -e "$item" ] || continue
            item=$(basename "$item")
            # sanitize to version only
            case "$item" in
                vmlinuz-*|vmlinux-*|config-*|initrd.img-*|System.map-*)
                    item=${item#*-}
                    ;;
                initramfs-*.img)
                    item=${item#*-}
                    item=${item%.img}
                    ;;
                *) ;;
            esac
            # belongs to current version
            case "$item" in
                $curk) continue;;
            esac
            # if it does not match, stay silent
            case "$x" in
                all|$item)
                    echo "$item"
                    ;;
            esac
        done
    done
}

list_kernels() {
    list_kernels_raw "$@" | sort -uV
}

prune_kernel() {
    [ -z "$1" ] && return
    echo "Pruning kernel: $1..."
    rm -rf /usr/lib/modules/apk-backup/"$1"
    rm -rf /usr/lib/modules/"$1"
    # make sure to remove anything that could be related to that kernel
    # it does not really matter whether it exists (so be quiet about it)
    for x in \
        config-$1 System.map-$1 vmlinux-$1 vmlinuz-$1 \
        initrd.img-$1 initramfs-$1.img; do
        rm -f /boot/$x
        rm -f /usr/lib/modules/apk-backup/$x
    done
}

case "$COMMAND" in
    list)
        if [ -z "$1" ]; then
            list_kernels all
        else
            list_kernels "$@"
        fi
        ;;
    rm)
        if [ -z "$1" ]; then
            usage() 1>&2
            exit 1
        fi
        if [ "$(id -u)" -ne 0 ]; then
            die "must be run as root"
        fi
        RUN_HOOKS=
        for kv in $(list_kernels "$@"); do
            prune_kernel "$kv"
            RUN_HOOKS=1
        done
        if [ -n "$RUN_HOOKS" ]; then
            echo "Running kernel hooks..."
            /usr/lib/base-kernel/run-kernel-d
        fi
        ;;
    *)
        usage
        exit 1
        ;;
esac
