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

ruff_output=""
if [ -n "$GITHUB_ACTIONS" ]; then
    # inline comment annotations
    ruff_output="--output-format github"
fi

if command -v ruff >/dev/null; then
    invoke ruff check $ruff_output
    invoke ruff format --diff --quiet
else
    invoke flake8 main contrib user src
    invoke find main contrib user src -name '*.py' -exec black --fast --check {} +
fi

# for local pre-push hooks that probably don't want to wait 10 seconds
if [ -z "$CI_SKIP_EXPENSIVE" ]; then
    invoke python3 cbuild relink-subpkgs
    invoke git diff --exit-code
    invoke python3 cbuild cycle-check
fi

exit $RET
