#!/bin/sh

RET=0

invoke() {
    printf "=> Running "
    printf "%s " "$@"
    printf "\n"
    "$@"

    if [ $? -ne 0 ]; then
        RET=1
    fi
}

if command -v ruff >/dev/null; then
    invoke ruff check
else
    invoke flake8 main contrib user src
fi

if command -v ruff >/dev/null; then
    invoke ruff format --diff
else
    invoke find main contrib user src -name '*.py' -exec black --fast --check {} +
fi

# for local pre-push hooks that probably don't want to wait 10 seconds
if [ -z "$CI_SKIP_EXPENSIVE" ]; then
    invoke python3.11 cbuild relink-subpkgs && git diff --exit-code
    invoke python3.11 cbuild cycle-check
fi

exit $RET
