#!/bin/sh

/usr/bin/systemd-sysusers || :
/usr/bin/systemd-tmpfiles --create --remove --exclude-prefix=/dev || :
