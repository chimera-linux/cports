#!/bin/sh

[ ! -d "/etc/kernel.d" ] && return 0

echo "Running kernel.d scripts..."

for f in /etc/kernel.d/*; do
    [ ! -f "$f" ] && continue # possibly empty
    $f || echo "FAILED: $f"
done

:
