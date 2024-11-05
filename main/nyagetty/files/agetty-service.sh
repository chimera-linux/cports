#!/bin/sh

case "$1" in
    tty[0-9]*|console) exec /usr/lib/agetty-default "$@" ;;
esac

exec /usr/lib/agetty-serial "$@"
