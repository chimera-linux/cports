#!/bin/sh
#
# A convenience wrapper for serial gettys. Takes the same arguments as
# the agetty helper script, but autodetects defaults (with fallbacks),
# also does not clear the screen by default.
#
# Copyright 2023-2024 q66 <q66@chimera-linux.org>
#
# License: BSD-2-Clause
#

GETTY="$1"
shift
GETTY_BAUD="$1"
shift
GETTY_TERM="$1"
shift
GETTY_8BIT=

detect_speed_proc() {
    local ttyn speed g8bit
    # sanitize the input string a bit
    ttyn=$1
    ttyn=${ttyn#/dev/}
    speed=$ttyn
    speed=${speed#*,}
    if [ "$speed" = "$ttyn" ]; then
        speed=
    fi
    ttyn=${ttyn%,*}
    # ensure it's the one we want
    [ "$ttyn" = "$GETTY" ] || return 0
    # ensure we were given some speed stuff
    [ -n "$speed" ] || return 0
    # ensure it exists
    [ -c "/dev/$ttyn" ] || return 0
    # parse
    case "$speed" in
        *n8*)
            speed=${speed%n*}
            g8bit=-8
            ;;
        *[oen]*)
            speed=${speed%o*}
            speed=${speed%e*}
            speed=${speed%n*}
            ;;
        *)
            # assume 8bit no parity
            g8bit=-8
            ;;
    esac
    echo "${speed}${g8bit}"
}

detect_speed_stty() {
    local ttyn speed cflags g8bit
    ttyn=$1
    # ensure it's a terminal
    speed=$(/usr/bin/stty -f "/dev/$ttyn" speed 2>/dev/null)
    if [ $? -ne 0 ]; then
        # not a terminal
        return 0
    fi
    cflags=$(stty -f "/dev/$ttyn" | grep "^cflags: " 2>/dev/null)
    if [ "$cflags" != "${cflags#*cs8 -parenb}" ]; then
        # detected 8bit no parity
        g8bit=-8
    fi
    echo "${speed}${g8bit}"
}

# first try to guess it from explicitly given cmdline
for x in $(cat /proc/cmdline); do
    case "$x" in
        console=*)
            [ -n "$GETTY_BAUD" ] || GETTY_BAUD=$(detect_speed_proc "${x#console=}")
            ;;
    esac
done

# then from stty...
[ -n "$GETTY_BAUD" ] || GETTY_BAUD=$(detect_speed_stty "$GETTY")

# split the -8 if needed
case "$GETTY_BAUD" in
    *-8)
        GETTY_8BIT=-8
        GETTY_BAUD=${GETTY_BAUD%-*}
        ;;
esac

# fallbacks for when we couldn't figure out anything...
[ -n "$GETTY_TERM" ] || GETTY_TERM=vt100
# default to 8bit no parity when detection failed
if [ -z "$GETTY_BAUD" ]; then
    case "$GETTY" in
        hvc[0-9]*) GETTY_BAUD=38400 ;;
        hvsi[0-9]*) GETTY_BAUD=19200 ;;
        *) GETTY_BAUD=115200 ;;
    esac
    GETTY_8BIT=-8
fi

exec /usr/lib/agetty-default "$GETTY" "$GETTY_BAUD" "$GETTY_TERM" $GETTY_8BIT -L --noclear "$@"
