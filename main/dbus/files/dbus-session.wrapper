#!/bin/sh

export DBUS_SESSION_BUS_ADDRESS="unix:path=/run/user/`id -u`/bus"

# export into activation environment to make it visible to other services
dinitctl setenv DBUS_SESSION_BUS_ADDRESS || :

exec dbus-daemon --session --address="$DBUS_SESSION_BUS_ADDRESS" "$@"
