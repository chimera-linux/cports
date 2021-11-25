#!/bin/sh
#
# Base system triggers.

trigger_shells() {
    # remove old shells db
    rm -f /etc/shells
    # none exist
    [ ! -d "/etc/shells.d" ] && return 0
    # incomplete system
    [ -z "$(command -v readlink)" ] && return 0

    echo "Regenerating /etc/shells..."

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
}

trigger_kernel() {
    [ ! -d "/etc/kernel.d" ] && return 0

    echo "Running kernel.d scripts..."

    for f in /etc/kernel.d/*; do
        [ ! -f "$f" ] && continue # possibly empty
        $f || echo "FAILED: $f"
    done
}

for trig in "$@"; do
    case "$trig" in
        /etc/shells.d*) trigger_shells;;
        /boot*) trigger_kernel;;
    esac
done

:
