#!/bin/sh

# restart the service instead of directly invoking the helper,
# as we don't want to mess with it in chroots with pseudofs mounted
if [ -S /run/dinitctl ]; then
    if /usr/bin/dinitctl --quiet is-started early-binfmt; then
        echo "Reloading binfmts..."
        /usr/bin/dinitctl restart early-binfmt || :
    fi
fi
