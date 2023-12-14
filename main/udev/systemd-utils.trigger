#!/bin/sh

# invoking sysusers is always harmless
/usr/bin/systemd-sysusers || :

# always create/remove/set
TMPFILES_ARGS="--create --remove"

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

/usr/bin/systemd-tmpfiles $TMPFILES_ARGS || :
