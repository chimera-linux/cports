#!/bin/sh

RET=0

if command -v ruff >/dev/null; then
    ruff check
else
    flake8 main contrib user src
fi

if [ $? -ne 0 ]; then
    RET=1
fi

if command -v ruff >/dev/null; then
    ruff format --diff
else
    find main contrib user src -name '*.py' -exec black --fast --check {} +
fi

if [ $? -ne 0 ]; then
    RET=1
fi

exit $RET
