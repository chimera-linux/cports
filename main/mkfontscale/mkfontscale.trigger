#!/bin/sh

set -e

for x in "$@"; do
    # this can be executed when a font dir is added or removed
    rm -f "${x}/fonts.dir"
    rm -f "${x}/fonts.scale"
    rmdir "${x}" > /dev/null 2>&1 || :
    # if cleaning up results in an empty dir, it's a removal trigger
    # otherwise, if it still exists, it's an install trigger, so index
    if [ -d "$x" ]; then
        mkfontdir "$x"
        mkfontscale "$x"
    fi
done
