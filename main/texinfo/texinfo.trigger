#!/bin/sh

rm -f /usr/share/info/dir

for f in $(find /usr/share/info -type f ! -name dir); do
    install-info "$f" /usr/share/info/dir 2>/dev/null || :
done
