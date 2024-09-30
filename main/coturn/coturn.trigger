#!/bin/sh

export PATH=/usr/bin

[ -f /var/lib/coturn/turndb ] && exit 0

mkdir -p /var/lib/coturn
sqlite3 /var/lib/coturn/turndb < /usr/share/turnserver/schema.sql
