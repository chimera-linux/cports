#!/bin/sh

/usr/bin/update-ca-certificates --fresh || :
# spawns some subprocesses, we want to let it finish
wait
