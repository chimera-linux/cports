#!/bin/sh

for d in "$@"; do
    [ -d "$d" ] && /usr/bin/update-mime-database "$d" > /dev/null 2>&1 || :
done
