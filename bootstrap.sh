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
# it is safe to remove masterdir-stage0 on failure. During any other
# stage, you should only remove the builddir/destdir inside.
#
# Additional options passed to this script are passed to cbuild.py. This
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

BASE_DATE="20210218"
BASE_URL="https://a-hel-fi.m.voidlinux.org/live/${BASE_DATE}"

case "$CARCH" in
    ppc64le)
        BASE_DATE="20200411"
        BASE_URL="https://repo.voidlinux-ppc.org/live/${BASE_DATE}"
        BASE_SHA256="9d0b17364dd5b44dc47fa18e7ba242f441049b2ae2d567d5cf0e9e19ff0366b9"
        ;;
    aarch64)
        BASE_SHA256="f550bbe36688e7276c020c96d60124ae77adf95268c2c4cf55ff8d1d8de86226"
        ;;
    x86_64)
        BASE_SHA256="07690d28eb8eebbb839af19bd4873689e6ed0fee53d271f0ce27e2edab8a3364"
        ;;
    *)
        echo "Unsupported architecture: $CARCH"
        exit 1
        ;;
esac

TARNAME="void-${CARCH}-musl-ROOTFS-${BASE_DATE}.tar.xz"

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
fi

if [ -z "${BOOTSTRAP_ROOT}" -o ! -d "${BOOTSTRAP_ROOT}" ]; then
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

cat << EOF > "${BOOTSTRAP_ROOT}/bootstrap-inner.sh"
# update base
echo ">> Updating base system..."
xbps-install -y -S || exit 1
xbps-install -yu xbps || exit 1
xbps-install -Syu || exit 1

# install dependencies
echo ">> Installing cbuild dependencies..."
xbps-install -y python3 pax-utils apk-tools openssl git bubblewrap || exit 1
echo ">> Installing build tools..."
xbps-install -y base-devel clang lld libcxx-devel llvm-libunwind-devel \
                cmake meson pkgconf bmake ninja byacc flex perl m4 || exit 1

cd /cports
python3 cbuild.py "\$@" bootstrap ${BOOTSTRAP_STAGE}
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
