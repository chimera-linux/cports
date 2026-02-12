#!/bin/sh
# generate systemd-boot kernel entries on kernel updates
gen-systemd-boot
# report error only if needed
RETC=$?
if [ $RETC -gt 1 ]; then
    exit $RETC
fi
exit 0
