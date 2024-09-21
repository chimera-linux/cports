#!/bin/sh
#
# a little wrapper that hides the ugly, only works for stage >0

# bypass the wrapper...
STRIP="/usr/bin/$STRIP"

die() {
    echo "$@" >&2
    exit 1
}

command -v "$STRIP" > /dev/null 2>&1 || die "$STRIP not found"
command -v "$OBJCOPY" > /dev/null 2>&1 || die "$OBJCOPY not found"

if [ "$1" = "-d" ]; then
    DO_SPLIT=1
    shift
fi

[ -d "$1" ] || die "DESTDIR does not exist"
DESTDIR="$1"
shift

[ -f "${DESTDIR}/$1" ] || die "input file does not exist"

set -e

SFILE="${DESTDIR}/$1"
DFILE="${DESTDIR}/usr/lib/debug/$1"
DPATH=$(dirname "$DFILE")

if [ -n "$DO_SPLIT" ]; then
    mkdir -p "$DPATH"
    "$OBJCOPY" --only-keep-debug "$SFILE" "$DFILE"
fi

"$STRIP" --strip-unneeded --remove-section=.comment --keep-section=.gnu_debuglink "$SFILE"

if [ -n "$DO_SPLIT" ]; then
    "$OBJCOPY" "--add-gnu-debuglink=$DFILE" "$SFILE"
fi

exit 0
