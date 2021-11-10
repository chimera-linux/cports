#!/bin/sh

CMD=/usr/bin/glib-compile-schemas
SPATH=/usr/share/glib-2.0/schemas

if [ -d "$SPATH" ]; then
    echo -n "Updating GSettings schemas in $SPATH..."
    if $CMD "$SPATH" > /dev/null 2>&1; then
        echo " done."
    else
        echo " failed!"
    fi
fi
