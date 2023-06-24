#!/bin/sh

export PATH=/usr/bin
set -e

for cfg in /etc/wireguard/*.conf; do
    [ -r "$cfg" ] || continue
    wg-quick "$1" "${cfg}"
done
