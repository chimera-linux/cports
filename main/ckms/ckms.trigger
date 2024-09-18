#!/bin/sh

set -e

export CKMS_APK_DEFER_INITRAMFS=1

[ -f /.cbuild_chroot_init ] && exit 0

# prune modules that are no longer installed

for mod in /var/lib/ckms/*; do
    [ -d "$mod" ] || continue
    for ver in "${mod}"/*; do
        [ -d "${ver}" ] || continue
        # skip the symlinks indicating installed modules
        [ -L "${ver}" ] && continue
        # if the module is invalid, just kill it
        if [ ! -f "${ver}/ckms.ini" ]; then
            rm -rf "${ver}"
            continue
        fi
        # otherwise check if still installed
        [ -d "${ver}/source" ] && continue
        # found a missing module; uninstall for every kernel
        for kern in /usr/lib/modules/*; do
            [ -d "${kern}" ] || continue
            kern="${kern#/usr/lib/modules/}"
            [ "${kern}" = "apk-backup" ] && continue
            ckms -q -k "${kern}" uninstall "${ver}" || :
        done
        # purge its state
        rm -rf "${ver}"
    done
done

# add new modules
for mod in /usr/src/*; do
    [ -d "${mod}" ] || continue
    [ -f "${mod}/ckms.ini" ] || continue
    ckms -q add "${mod}" > /dev/null 2>&1 || :
done

exec /usr/libexec/ckms-install-all
