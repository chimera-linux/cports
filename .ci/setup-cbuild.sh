#!/bin/sh

set -e

APK_VER="3.0.0_pre6-r0"
APK_URL="https://repo.chimera-linux.org/apk"
APK_ARCH=$(uname -m)
APK_FILE="apk-${APK_ARCH}-${APK_VER}.static"

echo "=> Getting apk-tools..."

wget "${APK_URL}/${APK_FILE}"
chmod +x "${APK_FILE}"

echo "=> Checking apk-tools..."

wget "${APK_URL}/sha256sums.txt"
grep "${APK_FILE}" sha256sums.txt|sha256sum --check

rm -f sha256sums.txt || :

echo "=> Setting up cbuild configuration..."
cat << EOF > etc/config.ini
[apk]
command = $(pwd)/${APK_FILE}
[build]
# they will not be packaged, but we can still CI them (no public artifacts)
allow_restricted = yes
timing = yes
EOF

echo "=> Generating cbuild key..."
python3.11 cbuild keygen

echo "... done setting up cbuild."
