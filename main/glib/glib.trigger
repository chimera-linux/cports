#!/bin/sh

if [ -d "/usr/share/glib-2.0/schemas" ]; then
    echo -n "Updating GSettings schemas in /usr/share/glib-2.0/schemas..."
    if /usr/bin/glib-compile-schemas "/usr/share/glib-2.0/schemas"; then
        echo " done."
    else
        echo " failed!"
    fi
fi
