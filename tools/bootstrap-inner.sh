#!/bin/sh
#
# This is the in-chroot part of the bootrapper.
#

# update base
echo ">> Updating base system..."
xbps-install -y -S || exit 1
xbps-install -yu xbps || exit 1
xbps-install -Syu || exit 1

# install dependencies
echo ">> Installing cbuild dependencies..."
xbps-install -y python3 pax-utils apk-tools openssl git bubblewrap || exit 1
echo ">> Installing build tools..."
xbps-install -y base-devel clang lld libcxx-devel llvm-libunwind-devel \
                cmake meson pkgconf bmake ninja byacc flex perl m4 || exit 1

cd /cports
python3 cbuild.py "$@" bootstrap
