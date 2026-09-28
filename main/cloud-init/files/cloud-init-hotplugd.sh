#!/bin/sh

PIPE="/run/cloud-init/hook-hotplug-cmd"

/usr/bin/mkfifo -m700 "$PIPE"

while :; do
    read args < "$PIPE"
    exec /usr/bin/cloud-init devel hotplug-hook $args
done

exit
