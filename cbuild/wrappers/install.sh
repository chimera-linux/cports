#!/bin/sh
# install-wrapper - run install(1), but never strip or chown
set -e

opts='bB:CcD:df:g:h:l:M:m:N:o:pSsT:Uv'

parsed="$(getopt -o "$opts" -n 'install-wrapper' -- "$@")"
eval set -- "$parsed"

# escape:
# - backslashes
# - double quotes
# - dollar signs (var expansion, expression eval)
# - backticks (expression eval)
quoteval() {
	printf '%s' "$1"|sed -e "s/\\\/\\\\\\\/g" \
		-e "s/\"/\\\\\"/g" -e "s/\\\$/\\\\\\$/g" \
		-e "s/\`/\\\\\\\`/g"
}

iopts=""
while :; do
	case "$1" in
	-g|-o)
		echo "install-wrapper: dropping option $1 $2." 1>&2
		shift 2;;
	-b|-c|-C|-d|-p|-S|-s|-U|-v)
		iopts="$iopts $1"
		shift;;
	-B|-D|-f|-h|-l|-M|-m|-N|-T)
		# arbitrary input, single quote the value
		ival=$(quoteval "$2")
		iopts="$iopts $1 \"$ival\""
		shift 2;;
	--)
		shift
		break;;
	*)
		echo 'cant happen, report a bug' 1>&2
		exit 111;;
	esac
done

iopts="$iopts --"

for arg in "$@"; do
	ival=$(quoteval "$arg")
	iopts="$iopts \"$ival\""
done

eval set -- "$iopts"

export STRIPBIN=/usr/bin/true
export DONTSTRIP=1

exec /usr/bin/install "$@"
