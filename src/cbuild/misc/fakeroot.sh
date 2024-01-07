#!/bin/sh
#
# This script is a part of cbuild. It exists because we want to ensure
# we are not using the janky launcher script that comes with fakeroot,
# at least not within our controlled sandbox.
#
# We don't really need most of its functionality in any case.

if [ ! -f "/.cbuild_fakeroot.sh" ]; then
    exec fakeroot "$@"
fi

unset FAKEROOTKEY

export FAKED_MODE="unknown-is-root"

KEY_PID=$(/usr/bin/faked)
FAKEROOTKEY=$(echo $KEY_PID | cut -d: -f1)
PID=$(echo $KEY_PID | cut -d: -f2)

trap "kill -s TERM $PID" EXIT INT

if [ -z "$FAKEROOTKEY" -o -z "$PID" ]; then
    echo >&2 "fakeroot: failed to start 'faked'"
    exit 1
fi

export FAKEROOTKEY
export LD_PRELOAD="/usr/lib/libfakeroot.so"

"$@"

exit $?
