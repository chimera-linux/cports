#!/bin/sh

if [ "$SOURCE_DATE_EPOCH" ]; then
	argspost="-u -r @$SOURCE_DATE_EPOCH"
fi
exec /usr/bin/date $args "$@"
