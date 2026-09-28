#!/bin/sh

[ ! -e /etc/rsyncd.conf ] && exit 1

exec /usr/bin/rsync --daemon --no-detach
