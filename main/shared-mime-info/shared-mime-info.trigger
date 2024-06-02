#!/bin/sh

# zoom zoom
export PKGSYSTEM_ENABLE_FSYNC=0

for d in "$@"; do
    [ -d "$d" ] && /usr/bin/update-mime-database "$d" > /dev/null 2>&1 || :
done
