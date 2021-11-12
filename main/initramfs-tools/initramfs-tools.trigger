#!/bin/sh

for arg in "$@"; do
    case "$arg" in
        /boot*) export TRIGGER_KERNEL=1;;
        /usr/share/initramfs-tools*) export TRIGGER_INITRAMFS=1;;
    esac
done

for f in /etc/initramfs-tools/triggers/*; do
    $f || echo "FAILED: $f"
done
