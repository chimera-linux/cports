#!/bin/sh

RET=0

flake8 main contrib user src
if [ $? -ne 0 ]; then
    RET=1
fi

find main contrib user src -name '*.py' -exec black --fast --check {} +
if [ $? -ne 0 ]; then
    RET=1
fi

exit $RET
