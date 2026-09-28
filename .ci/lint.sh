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

lint_targets="main user src"

if command -v ruff >/dev/null; then
    invoke ruff check $ruff_output $lint_targets
    invoke ruff format --diff --quiet $lint_targets
else
    invoke flake8 $lint_targets
    invoke find $lint_targets -name '*.py' -exec black --fast --check {} +
fi

# for local pre-push hooks that probably don't want to wait 10 seconds
if [ -z "$CI_SKIP_EXPENSIVE" ]; then
    invoke python3 cbuild relink-subpkgs
    invoke git diff --exit-code
    invoke python3 cbuild cycle-check
fi

exit $RET
