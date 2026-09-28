#!/bin/sh

for ic in "$@"; do
    rm -f "${ic}/icon-theme.cache" || :
    rmdir "$ic" > /dev/null 2>&1 || :
    if [ -d "$ic" ]; then
        /usr/bin/gtk-update-icon-cache -q -f -t "$ic" || :
    fi
done
