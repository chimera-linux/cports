#!/bin/sh

for x in "$@"; do
    case "$x" in
        *schemas*)
            /usr/bin/glib-compile-schemas "$x" > /dev/null 2>&1 || :
            ;;
        *modules*)
            /usr/bin/gio-querymodules "$x" > /dev/null 2>&1 || :
            ;;
        *) ;;
    esac
done
