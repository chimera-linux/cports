#!/bin/sh

echo "Regenerating man db..."
/usr/bin/makewhatis -Tutf8 || :
