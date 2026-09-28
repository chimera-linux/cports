#!/bin/sh
#
# depmod hook for ckms within chimera

if [ -n "$CKMS_APK_DEFER_DEPMOD" ]; then
    rm -f /usr/lib/modules/${1}/modules.dep
    exit 0
fi

if [ -f /boot/System.map-$1 ]; then
    exec depmod -a -F /boot/System.map-$1 $1
else
    exec depmod -a $1
fi
