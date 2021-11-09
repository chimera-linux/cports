#!/bin/sh
#
# Regenerates /etc/shells based on the contents of /etc/shells.d.

# remove old shells db
rm -f /etc/shells
# none exist
[ ! -d "/etc/shells.d" ] && exit 0
# incomplete system
[ -z "$(command -v readlink)" ] && exit 0

for shell in /etc/shells.d/*; do
    shp="$(readlink $shell)"
    if [ -n "$shp" -a -x "$shp" ]; then
        case "$shp" in
            /usr/bin*|/usr/sbin*)
                # canonical path
                echo "${shp}" >> /etc/shells
                # via /bin symlink
                echo "${shp#/usr}" >> /etc/shells
                ;;
            /*)
                echo "${shp}" >> /etc/shells
                ;;
        esac
    fi
done
