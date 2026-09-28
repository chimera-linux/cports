#!/bin/sh
#
# This is Chimera's implementation of Debian's linux-version script, written
# from scratch without a Perl dependency or dependency on any Debian stuff.
#
# I (q66 <q66@chimera-linux.org>) place this in the public domain.
#

PROGNAME=$0

usage() {
    cat << EOF
Usage: $PROGNAME compare VERSION1 OP VERSION2
       $PROGNAME sort [--reverse] [VERSION1 VERSION2 ...]
       $PROGNAME list [--paths]

The version arguments should be kernel version strings as shown by
'uname -r' and used in filenames.

The valid comparison operators are: lt le eq ge gt
EOF
}

error() {
    usage 1>&2
    exit 2
}

# 0 by default; do_cmp will treat input strings as versions as a whole
# if set to something else, it will strip whitespace followed by any
# extra string before treating it as a version, meant for sort with stdin
STRIP_MODE=0

do_cmp() {
    # strict args
    if [ $# -ne 3 ]; then
        error
    fi
    # sanitize operator
    OP=$2
    case "$OP" in
        lt) OP="<";;
        le) OP="<=";;
        eq) OP="=";;
        gt) OP=">";;
        ge) OP=">=";;
        *) error ;;
    esac
    # versions and normalized versions
    VER1=$1
    VER2=$3
    if [ $STRIP_MODE -ne 0 ]; then
        # sanitize the versions
        VER1=$(echo "$VER1" | grep -E -o "^[ ]*[^ ]+")
        VER2=$(echo "$VER2" | grep -E -o "^[ ]*[^ ]+")
    fi
    # do a compare, apk version will take any string, it will only
    # compare the valid version part of the string and ignore the rest
    case $(apk version -q -t $VER1 $VER2) in
        \<) test "$OP" = "<" -o "$OP" = "<=" ;;
        \>) test "$OP" = ">" -o "$OP" = ">=" ;;
        *)
            # lexicographical comparison
            expr "$VER1" "$OP" "$VER2" > /dev/null
            ;;
    esac
}

SORT_OP="lt"

cmp_vers() {
    do_cmp "$1" $SORT_OP "$2"
}

quoteval() {
    if [ $STRIP_MODE -eq 0 ]; then
        # safe to assume there are no quotes, don't waste time
        printf "%s" "$1"
    else
        printf "%s" "$1" | sed -e "s/\\\/\\\\\\\/g" \
            -e "s/\"/\\\\\"/g" -e "s/\\\$/\\\\\\$/g" \
            -e "s/\`/\\\\\\\`/g"
    fi
}

quoteprint() {
    lval=$(quoteval "$1")
    printf "%s" "\"$1\" "
}

insert_one() {
    X="$1"
    shift
    while [ $# -gt 0 ] && cmp_vers "$1" "$X"; do
        quoteprint "$1"
        shift
    done
    quoteprint "$X"
    while [ $# -gt 0 ]; do
        quoteprint "$1"
        shift
    done
}

do_sort() {
    if [ "$1" = "--reverse" ]; then
        SORT_OP="gt"
        shift
    fi
    # read on standard input if no args
    if [ $# -eq 0 ]; then
        ARGS=""
        while read line; do
            lval=$(quoteval "$line")
            ARGS="$ARGS \"$lval\""
        done
        eval set -- "$ARGS"
    fi
    # sort the list
    for p in "$@"; do
        if [ -z "$initial" ]; then
            initial=1
            # clear the arglist once the for loop has picked it up
            set --
        fi
        eval set -- $(insert_one "$p" "$@")
    done
    while [ $# -gt 0 ]; do
        echo $1
        shift
    done
}

do_list() {
    [ $# -gt 1 ] && error
    [ $# -eq 1 -a "$1" != "--paths" ] && error
    # none for some reason
    [ -d /boot ] || exit 0
    # process vmlinu[xz]
    for kern in /boot/vmlinu[xz]-*; do
        # handle the no-kernels case
        [ ! -f "$kern" ] && continue
        # this should be a kernel
        if [ $# -eq 1 ]; then
            echo ${kern#*-} $kern
        else
            echo ${kern#*-}
        fi
    done
}

# no args
if [ $# -eq 0 ]; then
    error
fi

CMD=$1
shift

case "$CMD" in
    compare) do_cmp "$@" ;;
    sort) do_sort "$@" ;;
    list) do_list "$@" | sort ;;
    --help) usage ;;
    *) error ;;
esac
