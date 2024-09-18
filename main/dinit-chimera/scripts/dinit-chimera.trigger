#!/bin/sh

set -e

services=

for x in "$@"; do
    case "$x" in
        *swclock*)
            # update the timestamp to system clock every time
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
    /usr/bin/dinitctl --quiet is-started "$service" || continue
    echo "Restarting ${service}..."
    /usr/bin/dinitctl restart "$service" || :
done
