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

exit $RET
