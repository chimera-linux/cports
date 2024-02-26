#!/bin/sh

# transition nobody/nogroup
if [ "$(/usr/bin/id -u nobody)" = "99" ]; then
    /usr/bin/echo "CAUTION: nobody user id is 99, transitioning to 65534." || :
    /usr/bin/echo "It is recommended that you reboot after this change." || :
    /usr/bin/groupmod -g 65534 nogroup || :
    /usr/bin/usermod -u 65534 -g 65534 nobody || :
fi

/usr/bin/pwconv && /usr/bin/grpconv || :
