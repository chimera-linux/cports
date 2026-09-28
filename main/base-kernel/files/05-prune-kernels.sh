#!/bin/sh

# number of backups to keep by default (1 non-managed)
KERNEL_NUM_BACKUPS=1

[ -e /etc/default/kernel ] && . /etc/default/kernel

# if manually invoked with "all", don't keep any backups
if [ "$1" = "all" ]; then
    KERNEL_NUM_BACKUPS=0
fi

# if invalid, fall back to default
if ! [ "$KERNEL_NUM_BACKUPS" -ge 0 ] 2>/dev/null; then
    KERNEL_NUM_BACKUPS=1
fi

APK_KSERS=
RAW_KVERS=
# first collect the kernel list
for kpath in /usr/lib/modules/*; do
    # may mean we did not match anything
    [ -d "$kpath" ] || continue
    # skip what does not have an apk marker, e.g. old-style kernels
    [ -f "${kpath}/.apk-series" ] || continue
    # extract the version
    kver=$(basename "$kpath")
    # append
    RAW_KVERS="$RAW_KVERS $kver"
    # only track installed kernels here
    [ -f "${kpath}/apk-dist/.apk-series" ] || continue
    # if we're not keeping backups, don't try
    [ "$KERNEL_NUM_BACKUPS" -lt 1 ] && continue
    # grab the series name...
    kser=$(cat "${kpath}/apk-dist/.apk-series")
    # it must be non-empty, handle that first
    [ -n "$kser" ] || continue
    # it must be a simple package name so it does not break fragile shell stuff
    vkser=$(echo "$kser" | grep -o "[a-zA-Z0-9.-]*")
    [ "$kser" = "$vkser" ] || continue
    # finally add it...
    APK_KSERS="${APK_KSERS}${kser}:${KERNEL_NUM_BACKUPS}:"
done

set -- $RAW_KVERS
# nothing...
[ $# -gt 0 ] || exit 0

# revsorted list of apk-managed versions
KVERS=$(linux-version sort --reverse "$@")

# now go over them...
for kver in $KVERS; do
    kpath="/usr/lib/modules/${kver}"
    # if currently installed, skip
    [ -f "${kpath}/apk-dist/.apk-series" ] && continue
    kser=$(cat "${kpath}/.apk-series")
    # sanitize, don't touch if the series is not specifically known
    [ -n "$kser" ] || continue
    # try extracting the count...
    bakstr=$(echo "$APK_KSERS" | grep -o "${kser}:[0-9][0-9]*:")
    if [ -z "$bakstr" ]; then
        # not matched, prune unless currently booted
        [ "$kver" = "$(uname -r)" ] && continue
        echo "Pruning obsolete kernel: ${kver}..."
        rm -f /boot/*-"$kver"
        rm -f /boot/initramfs-"$kver".img
        rm -rf "/boot/dtbs/dtbs-$kver"
        rm -rf "/usr/lib/modules/$kver"
        continue
    fi
    # decrement the count
    bakc=$(echo "$bakstr" | cut -d: -f2)
    bakc=$(($bakc - 1))
    # remove from matchers...
    APK_KSERS=$(echo "$APK_KSERS" | sed "s,${bakstr},,")
    # if the count is still >= 1, add it back
    if [ "$bakc" -gt 0 ]; then
        APK_KSERS="${APK_KSERS}${kser}:${bakc}:"
    fi
done

# prune invalid leftovers from the transition
for kpath in /usr/lib/modules/*; do
    [ -d "$kpath" ] || continue
    [ -f "${kpath}/modules.order" ] || continue
    [ -f "${kpath}/.apk-series" ] && continue
    kver=${kpath#/usr/lib/modules/}
    [ -f "/boot/config-${kver}" ] && continue
    rm -rf "${kpath}"
done

exit 0
