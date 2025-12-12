#!/bin/sh

for x in "$@"; do
    case "$x" in
        *rules.d*)
            if [ -S /run/udev/control ]; then
                    /usr/bin/udevadm control --reload || :
            fi
            ;;
        *hwdb.d*)
            echo "Updating hwdb..."
            /usr/bin/systemd-hwdb update || :
            ;;
    esac
done
