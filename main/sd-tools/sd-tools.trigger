#!/bin/sh

set -e

# invoking sysusers is always harmless
/usr/bin/sd-sysusers || :

# always create/remove/set
# always skip messing with resolv.conf during package configuration,
# we don't want things to change under the users' hands, instead leave
# it to when it's safer (after boot)
TMPFILES_ARGS="--create --remove --replace /usr/lib/tmpfiles.d/resolv.conf -"

# a little heuristical but unassuming with userland
# the idea is that if /run is mounted, it's probably a running system
# (doesn't matter if container or real) and has pseudo-filesystems
# in place, otherwise we avoid messing with them
if [ ! -r /proc/self/mounts -o ! -x /usr/bin/awk ]; then
    # bare system, don't mess with pseudofs
    TMPFILES_ARGS="$TMPFILES_ARGS -E"
else
    RUN_FSTYPE=$(/usr/bin/awk '{if ($2 == "/run") print $1;}' /proc/self/mounts)
    if [ "$RUN_FSTYPE" != "tmpfs" ]; then
        # /run is not mounted or is something bad, don't mess with pseudofs
        TMPFILES_ARGS="$TMPFILES_ARGS -E"
    fi
fi

/usr/bin/echo | /usr/bin/sd-tmpfiles $TMPFILES_ARGS || :
