# Sets up locale system settings from /etc/locale.conf.
#
if [ -e /etc/locale.conf ]; then
    . /etc/locale.conf
else
    # defaults
    LANG=C.UTF-8
    LC_COLLATE=C
fi

export LANG LANGUAGE LC_CTYPE LC_NUMERIC LC_TIME LC_COLLATE LC_MONETARY
export LC_MESSAGES LC_PAPER LC_NAME LC_ADDRESS LC_TELEPHONE LC_MEASUREMENT
export LC_INDENTIFICATION
