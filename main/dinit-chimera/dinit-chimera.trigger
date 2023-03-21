#!/bin/sh

# restart the service instead of directly invoking the helper,
# as we don't want to mess with it in chroots with pseudofs mounted
if [ -S /run/dinitctl ]; then
    DOUT=$(/usr/bin/dinitctl status init-binfmt 2>&1|/usr/bin/grep State:)
    echo "Reloading binfmts..."
    case "$DOUT" in
        *STARTED) /usr/bin/dinitctl restart init-binfmt || :
    esac
fi
