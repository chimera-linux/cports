# Check for interactive bash
[ -z "$BASH_VERSION" -o -z "$PS1" ] && return

# Bash login shells only run /etc/profile
# Bash non-login shells run only /usr/share/bash/bashrc
# We want to source /usr/share/bash/bashrc in any case
. /usr/share/bash/bashrc
