#!/bin/sh

# this may run out of order with sd-tools trigger, invoke the right parts
/usr/bin/sd-sysusers /usr/lib/sysusers.d/flatpak.conf
/usr/bin/sd-tmpfiles --create /usr/lib/tmpfiles.d/flatpak.conf
# and do the rest
/usr/bin/flatpak remote-list > /dev/null 2>&1

exit 0
