#!/bin/sh
set -eu
ARCH_TARGET=$1
sed -i '' "s/@TRIPLE@/$ARCH_TARGET/g;" mingw-configure.sh
