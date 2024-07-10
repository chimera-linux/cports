#!/bin/sh

RET=0

if command -v ruff >/dev/null; then
    echo "=> Running ruff check"
    ruff check
else
    echo "=> Running flake8"
    flake8 main contrib user src
fi

if [ $? -ne 0 ]; then
    RET=1
fi

if command -v ruff >/dev/null; then
    echo "=> Running ruff format --diff"
    ruff format --diff
else
    echo "=> Running black --check"
    find main contrib user src -name '*.py' -exec black --fast --check {} +
fi

if [ $? -ne 0 ]; then
    RET=1
fi

exit $RET
