#!/bin/sh

/usr/bin/update-ca-certificates --fresh &> /dev/null || :
# spawns some subprocesses, we want to let it finish
wait
