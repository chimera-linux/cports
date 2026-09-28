#!/bin/sh

echo "Updating fonts cache..."

fc-cache --system-only > /dev/null || :
