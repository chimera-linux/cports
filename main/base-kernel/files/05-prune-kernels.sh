#!/bin/sh

# number of backups to keep by default (2 latest)
KEEP_BACKUP=2

# if manually invoked with "all", don't keep any backups
if [ "$1" = "all" ]; then
    KEEP_BACKUP=0
fi

RAW_KVERS=
# get a list of all apk-managed kernels
for kpath in /usr/lib/modules/*; do
    # may mean we did not match anything
    [ -d "$kpath" ] || continue
    # skip what does not have an apk marker
    [ -f "${kpath}/.apk-kernel" ] || continue
    # extract the version
    kver=$(basename "$kpath")
    # append
    RAW_KVERS="$RAW_KVERS $kver"
done

set -- $RAW_KVERS
# nothing...
[ $# -gt 0 ] || exit 0

# sorted list of apk-managed versions
KVERS=$(linux-version sort "$@")

# now go over them...
for kver in $KVERS; do
    # skip if current uname
    [ "$kver" = "$(uname -r)" ] && continue
    # skip if installed
    [ -d "/usr/lib/modules/apk-dist/$kver" ] && continue
    # make up a regex pattern to match specific series
    mkpat=$(echo "$kver" | sed 's,\([0-9]*\)\.\([0-9]*\)\..*-\(.*\),^\1\\.\2\\..*-\3$,')
    # skip $KEEP_BACKUP in the series
    case $(echo $KVERS | tr ' ' '\n' | grep "$mkpat" | tail -n $KEEP_BACKUP) in
        $kver) continue ;;
    esac
    # remove anything else...
    echo "Pruning obsolete kernel: ${kver}..."
    rm -f /boot/*-$kver
    rm -rf "/boot/dtbs/dtbs-$kver"
    rm -rf "/usr/lib/modules/$kver"
done

exit 0
