#!/bin/sh

for kpath in /usr/lib/modules/apk-dist/*; do
    # probably means we did not match anything...
    [ -d "$kpath" ] || continue
    # extract the version
    kver=$(basename "$kpath")
    tpath="/usr/lib/modules/$kver"
    # if already copied, skip
    [ -d "$tpath" ] && continue
    echo "Setting up new kernel: ${kver}..."
    # setup, hardlink things
    if ! cp -la "$kpath" "$tpath"; then
        # clean up just in case
        rm -rf "$tpath"
        echo "SETUP FAILED: $kver"
        continue
    fi
    # deal with boot files
    for bfile in "${tpath}/boot/"*; do
        [ -e "$bfile" ] || break
        # dtbs may be a directory...
        if [ -d "$bfile" ]; then
            # maybe come up with a more robust way later
            mv "${bfile}/"* /boot/$(basename "$bfile")
        else
            mv "$bfile" /boot
        fi
    done
    # clean up
    rm -rf "${tpath}/boot"
    # create marker
    touch "${tpath}/.apk-kernel"
done

exit 0
