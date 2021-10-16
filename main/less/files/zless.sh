#!/bin/sh
#
# Source: FreeBSD (2021/10/16)
#

export LESSOPEN="||/usr/bin/lesspipe.sh %s"
exec /usr/bin/less "$@"
