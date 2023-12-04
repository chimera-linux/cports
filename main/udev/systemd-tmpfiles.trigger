#!/bin/sh

/usr/bin/systemd-tmpfiles --create --remove --exclude-prefix=/dev || :
