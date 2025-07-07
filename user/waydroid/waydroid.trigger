#!/bin/sh

# perform expected/required version migrations for smooth upgrades
[ -f /var/lib/waydroid/waydroid.cfg ] || exit 0
/usr/bin/waydroid upgrade --offline
