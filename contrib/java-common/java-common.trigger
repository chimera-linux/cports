#!/bin/sh

PROFILE="/etc/profile.d/java-jre.sh"
mkdir -p /etc/profile.d
rm -f "$PROFILE" || :

JAVA_BIN=$(readlink -f /usr/bin/java || :)
[ -x "$JAVA_BIN" -a "$JAVA_BIN" != "/usr/bin/java" ] || exit 0

JAVA_HOME="${JAVA_BIN%/bin/java}"
[ -d "$JAVA_HOME" ] || exit 0

echo "Updating JAVA_HOME..."

cat << EOF > "$PROFILE"
export JAVA_HOME="$JAVA_HOME"
EOF
