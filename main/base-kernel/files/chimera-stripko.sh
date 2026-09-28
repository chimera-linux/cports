#!/bin/sh

RETV=0
RETC=0

if [ -x /usr/bin/llvm-strip ]; then
    STRIP=/usr/bin/llvm-strip
    OBJCOPY=/usr/bin/llvm-objcopy
else
    STRIP=/usr/bin/strip
    OBJCOPY=/usr/bin/objcopy
fi

case "$1" in
    --strip-module)
        DPATH=
        ;;
    --strip-module=*)
        DPATH=${1#--strip-module=}
        ;;
    *)
        exec "$STRIP" "$@"
        ;;
esac

# first arg
shift

if [ -n "$DPATH" ]; then
    mkdir -p "$DPATH"
fi

while [ $# -gt 0 ]; do
    if [ -n "$DPATH" ]; then
        MODP=${1#${INSTALL_MOD_PATH}}
        if [ "${1%/*}" != "$1" ]; then
            mkdir -p "${DPATH}/${MODP%/*}"
        fi
        "$OBJCOPY" --only-keep-debug --compress-debug-sections "$1" "${DPATH}/$MODP"
        RETC=$?
        if [ $RETC -eq 0 ]; then
            "$OBJCOPY" "--add-gnu-debuglink=${DPATH}/$MODP" "$1"
            RETC=$?
        fi
        [ $RETC -ne 0 -a $RETV -eq 0 ] && RETV=$RETC
    fi
    "$STRIP" --strip-debug "$1"
    RETC=$?
    [ $RETC -ne 0 -a $RETV -eq 0 ] && RETV=$RETC
    shift
done

exit $RETV
