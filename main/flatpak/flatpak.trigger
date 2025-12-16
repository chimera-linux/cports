#!/bin/sh

# this may run out of order with the main trigger, invoke the right parts
/usr/bin/systemd-sysusers /usr/lib/sysusers.d/flatpak.conf
/usr/bin/systemd-tmpfiles --create /usr/lib/tmpfiles.d/flatpak.conf
# and do the rest
/usr/bin/flatpak remote-list > /dev/null 2>&1

exit 0
