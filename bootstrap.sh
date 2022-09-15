#!/bin/sh
#
# This script will bootstrap Chimera on any Linux system. It works by setting
# up a binary system for bootstrap, then following the standard procedure.
#
# NOTE: generate and set up a signing key with cbuild as you would normally
# (follow the README). This will be used to sign the packages just like if
# you ran it unwrapped.
#
# If the process fails at any point, you can re-run with BOOTSTRAP_ROOT
# set in the environment to make it continue. During stage 0 bootstrap,
# it is safe to remove bldroot-stage0 on failure. During any other
# stage, you should only remove the builddir/destdir inside.
#
# Additional options passed to this script are passed to cbuild. This
# is most useful to set the number of jobs (e.g. -j16).
#

if ! command -v "bwrap" > /dev/null; then
    echo "Bubblewrap not found!"
    exit 1
fi

if ! command -v "curl" > /dev/null; then
    echo "Curl not found!"
    exit 1
fi

if ! command -v "sha256sum" > /dev/null; then
    echo "Sha256sum not found!"
    exit 1
fi

CARCH=$(uname -m)

# container

BASE_DATE="20220912"
BASE_URL="https://repo.chimera-linux.org/live/${BASE_DATE}"
BOOTSTRAP_APK="apk"

case "$CARCH" in
    ppc64le)
        BASE_SHA256="f5cb3512184ec540e98e8bbb4add69eecd8454ad791396fd3b88654d5a7cf22c""
        ;;
    aarch64)
        BASE_SHA256="3331b1b139f6501c38da7f9e1ba693c5c981612e701806f3c4266caaf610dfde"
        ;;
    x86_64)
        BASE_SHA256="7c5e511b6e6053a4b2b8ed1e978bb87c27a3e01c4c10e1a4b83f4e0f7e86af7f"
        ;;
    *)
        echo "Unsupported architecture: $CARCH"
        exit 1
        ;;
esac

TARNAME="chimera-linux-${CARCH}-ROOTFS-${BASE_DATE}-core.tar.gz"

# fetch container

if [ ! -f "${TARNAME}" ]; then
    echo "Fetching base tarball..."

    ! test -f "${TARNAME}" && curl "${BASE_URL}/${TARNAME}" -o "${TARNAME}"

    if [ $? -ne 0 ]; then
        echo "Failed to fetch base tarball"
        exit 1
    fi
fi

if [ -z "${BOOTSTRAP_ROOT}" -o ! -d "${BOOTSTRAP_ROOT}" ]; then
    echo "${BASE_SHA256} ${TARNAME}" | sha256sum --check

    if [ $? -ne 0 ]; then
        echo "Failed to verify base tarball"
        exit 1
    fi

    if [ -z "${BOOTSTRAP_ROOT}" ]; then
        BOOTSTRAP_ROOT=$(mktemp -d "bootstrap.XXXXXXXXXX")
    
        if [ $? -ne 0 ]; then
            echo "Failed to create bootstrap directory"
            exit 1
        fi
    else
        mkdir "${BOOTSTRAP_ROOT}"
        if [ $? -ne 0 ]; then
            echo "Failed to create bootstrap directory ${BOOTSTRAP_ROOT}"
            exit 1
        fi
    fi

    cd "${BOOTSTRAP_ROOT}"

    tar xf "../${TARNAME}"

    if [ $? -ne 0 ]; then
        echo "Failed to extract bootstrap root"
        exit 1
    fi

    cd ..
fi

cp /etc/resolv.conf "${BOOTSTRAP_ROOT}/etc"
mkdir -p "${BOOTSTRAP_ROOT}/cports"

if [ -z "${BOOTSTRAP_STAGE}" ]; then
    BOOTSTRAP_STAGE="2"
fi

do_apk() {
    FAKEROOTDONTTRYCHOWN=1 fakeroot -- ${BOOTSTRAP_APK} \
        --root "${BOOTSTRAP_ROOT}" "$@"
    if [ "$?" -ne 0 ]; then
        echo "Command failed: apk $@"
        exit 1
    fi
}
echo ">> Updating base system..."
do_apk update
do_apk upgrade --available
echo ">> Installing cbuild bootstrap tools..."
do_apk add --no-scripts base-cbuild-bootstrap
# generate inner script
cat << EOF > "${BOOTSTRAP_ROOT}/bootstrap-inner.sh"
cd /cports
CBUILD_APK_PATH=/usr/bin/apk ./cbuild "\$@" bootstrap ${BOOTSTRAP_STAGE}
EOF

bwrap --unshare-user \
    --bind "${BOOTSTRAP_ROOT}" "/" \
    --dev /dev --proc /proc --tmpfs /tmp \
    --bind "$(pwd)" /cports \
    /bin/sh /bootstrap-inner.sh "$@"

if [ $? -ne 0 ]; then
    echo "Bootstrap failed!"
    exit 1
fi

exit 0
