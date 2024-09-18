#!/bin/sh

set -e

export PATH=/usr/bin

# transition nobody/nogroup
if [ "$(id -u nobody)" = "99" ]; then
    echo "CAUTION: nobody user id is 99, transitioning to 65534." || :
    echo "It is recommended that you reboot after this change." || :
    groupmod -g 65534 nogroup || :
    usermod -u 65534 -g 65534 nobody || :
fi

# transition tty presumably from cdrom
TTY_GID=$(getent group tty | cut -d: -f3)
if [ "$TTY_GID" != "5" ]; then
    OTHER_NAME=$(getent group 5 | cut -d: -f1)
    echo "CAUTION: tty gid is $TTY_GID, transitioning to 5." || :
    echo "This currently belongs to '$OTHER_NAME' and will swap." || :
    echo "It is recommended that you reboot after this change." || :
    groupmod -o -g "$TTY_GID" "$OTHER_NAME" || :
    groupmod -o -g 5 tty || :
fi

pwconv && grpconv || :
