#!/bin/sh
#
# Adapted from Alpine Linux

for f in /etc/chromium/*.conf; do
  [ -f "$f" ] && . "$f"
done

# the defaults to use if nothing else is defined
if [ -z "${CHROMIUM_FLAGS+x}" ]; then
  CHROMIUM_FLAGS="--ozone-platform-hint=auto"
fi

# Append CHROMIUM_USER_FLAGS (from env) on top of system
# default CHROMIUM_FLAGS (from /etc/chromium/chromium.conf).
CHROMIUM_FLAGS="$CHROMIUM_FLAGS ${CHROMIUM_USER_FLAGS:+"$CHROMIUM_USER_FLAGS"}"

# Let the wrapped binary know that it has been run through the wrapper
export CHROME_WRAPPER="$(readlink -f "$0")"

PROGDIR=${CHROME_WRAPPER%/*}

case ":$PATH:" in
*:$PROGDIR:*)
  # $PATH already contains $PROGDIR
  ;;
*)
  # Append $PROGDIR to $PATH
  export PATH="$PATH:$PROGDIR"
  ;;
esac

if [ $(id -u) -eq 0 ] && [ $(stat -f %u -L ${XDG_CONFIG_HOME:-${HOME}}) -eq 0 ]; then
  # Running as root with HOME owned by root.
  # Pass --user-data-dir to work around upstream failsafe.
  CHROMIUM_FLAGS="--user-data-dir=${XDG_CONFIG_HOME:-"$HOME"/.config}/chromium $CHROMIUM_FLAGS"
fi

# Set the .desktop file name
export CHROME_DESKTOP="chromium.desktop"
export CHROME_VERSION_EXTRA="Chimera Linux"

cd "$PROGDIR" || exit 1

exec "./chromium" ${CHROMIUM_FLAGS} "$@"
