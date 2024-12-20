#!/bin/sh

export PATH=/usr/bin

set -e

# remove old shells db
rm -f /etc/shells /etc/shells.tmp
# none exist
[ ! -d "/etc/shells.d" -a ! -d "/usr/lib/shells.d" ] && exit 0

echo "Regenerating /etc/shells..."

for shell in /etc/shells.d/* /usr/lib/shells.d/*; do
    shp="$(readlink $shell || :)"
    if [ -n "$shp" -a -x "$shp" ]; then
        case "$shp" in
            /usr/bin*|/usr/sbin*)
                # canonical path
                echo "${shp}" >> /etc/shells.tmp
                # via /bin symlink
                echo "${shp#/usr}" >> /etc/shells.tmp
                ;;
            /*)
                echo "${shp}" >> /etc/shells.tmp
                ;;
        esac
    fi
done

cat /etc/shells.tmp | sort | uniq > /etc/shells
rm -f /etc/shells.tmp

:
