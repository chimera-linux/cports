#!/bin/sh

for x in "$@"; do
    case "$x" in
        *swclock*)
            # update the timestamp to system clock every time
            touch /var/lib/swclock/timestamp > /dev/null 2>&1 || :
            ;;
        *binfmt*)
            # restart the service instead of directly invoking the helper,
            # as we don't want to mess with it in chroots with pseudofs mounted
            if [ -S /run/dinitctl ]; then
                if /usr/bin/dinitctl --quiet is-started early-binfmt; then
                    echo "Reloading binfmts..."
                    /usr/bin/dinitctl restart early-binfmt || :
                fi
            fi
            ;;
    esac
done
