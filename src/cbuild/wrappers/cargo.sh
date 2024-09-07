#!/bin/sh

if [ -n "$CBUILD_NO_CARGO_AUDITABLE" ]; then
    exec /usr/bin/cargo "$@"
elif command -v cargo-auditable >/dev/null; then
    exec /usr/bin/cargo auditable "$@"
else
    exec /usr/bin/cargo "$@"
fi
