#!/bin/sh
set -euv
ARCH_TARGET=$1

sed "s/@TRIPLE@/$ARCH_TARGET/g;" meson-mingw-wrapper > $ARCH_TARGET-meson

cat <<EOF > Makefile
toolchain-$ARCH_TARGET.meson:
	@python toolchain_generator.py --arch $ARCH_TARGET --output-file \$@
EOF
