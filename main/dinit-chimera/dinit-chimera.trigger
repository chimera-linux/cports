#!/bin/sh

export PATH=/usr/bin

set -e

services=

for x in "$@"; do
    case "$x" in
        *dinit.d*)
            # update the timestamp to system clock every time
            mkdir -p /var/lib/swclock > /dev/null 2>&1 || :
            touch /var/lib/swclock/timestamp > /dev/null 2>&1 || :
            ;;
        *modules-load*|*modprobe*)
            case "$services" in
                *early-modules*) ;;
                *) services="$services early-modules" ;;
            esac
            ;;
        *binfmt*)
            case "$services" in
                *early-binfmt*) ;;
                *) services="$services early-binfmt" ;;
            esac
            ;;
    esac
done

[ -S /run/dinitctl ] || exit 0

for service in $services; do
    dinitctl --quiet is-started "$service" || continue
    echo "Restarting ${service}..."
    dinitctl restart "$service" || :
done
