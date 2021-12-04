#!/bin/sh

if [ -n "$CBUILD_BYPASS_STRIP_WRAPPER" ]; then
    exec /usr/bin/${0##*/} "$@"
fi

STRIPOUT=

while getopts ":o:" opt; do
    case "$opt" in
        o) STRIPOUT=$OPTARG;;
    esac
done

shift "$((OPTIND - 1))"

if [ -n "$STRIPOUT" ]; then
    if [ "$#" -ne 1 ]; then
        exit 1
    fi
    ln "$@" "$STRIPOUT"
elif [ "$#" -eq 0 ]; then
    exit 1
else
    exit 0
fi
