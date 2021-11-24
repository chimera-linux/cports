#!/bin/sh

for f in /etc/initramfs-tools/triggers/*; do
    $f || echo "FAILED: $f"
done
