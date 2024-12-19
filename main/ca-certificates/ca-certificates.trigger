#!/bin/sh

# pre-create emptydirs if needed
/usr/bin/sd-tmpfiles --create /usr/lib/tmpfiles.d/ca-certificates.conf

# don't fail if it fails
/usr/bin/update-ca-certificates || :
