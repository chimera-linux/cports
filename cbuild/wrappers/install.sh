#!/bin/sh
# install-wrapper - run install(1), but never strip or chown
set -e

# taken from install (GNU coreutils) 8.23
opts='bcCdDg:m:o:psS:t:TvZ'
longopts='backup::,compare,directory,group:,mode:,owner:,preserve-timestamps,\
strip:,strip-program:,suffix:,target-directory:,no-target-directory,verbose,\
preserve-context,context::,help,version'

parsed="$(getopt -o "$opts" --long "$longopts" -n 'install-wrapper' -- "$@")"
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
	-s|--strip)
		echo "install-wrapper: overriding call to strip(1)." 1>&2
		iopts="$iopts $1 --strip-program=true"
		shift;;
	--strip-program)
		echo "install-wrapper: dropping strip program '$2'." 1>&2
		shift 2;;
	-g|--group|-o|--owner)
		echo "install-wrapper: dropping option $1 $2." 1>&2
		shift 2;;
	-b|-c|-C|--compare|-d|--directory|-D|-p|--preserve-timestamps|\
	-T|--no-target-directory|-v|--verbose|--preserve-context|-Z|\
	--help|--version)
		iopts="$iopts $1"
		shift;;
	-m|--mode|-S|--suffix|-t|--target-directory|--backup|--context)
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

exec /usr/bin/install ./test2.sh "$@"
