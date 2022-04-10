#!/bin/sh
# only needed when the logo changes

if ! command -v rsvg-convert >/dev/null; then
    echo "Please install librsvg-progs"
    exit 1
fi

rm -rf ./icons && mkdir icons

RESOLUTIONS="16 22 32 48 64 128 256 512 1024"

for res in $RESOLUTIONS; do
    rsvg-convert chimera-logo.svg --keep-aspect-ratio --width $res -o ./icons/chimera-logo-$res.png
done

rsvg-convert chimera-logo.svg --format svg -o ./icons/chimera-logo.svg
