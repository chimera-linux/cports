#!/bin/sh
#
# This is a helper script to simplify building Chimera kernels.
#
# Usage:
#
# $ chimera-buildkernel prepare [opts]
# $ chimera-buildkernel config [tgt] # tgt is menuconfig by default
# $ chimera-buildkernel build
# $ chimera-buildkernel install <destdir>
# $ chimera-buildkernel clean
#
# I (q66 <q66@chimera-linux.org>) hereby place this script in the public domain.
#

PROGNAME=$0

usage() {
    cat << EOF
Usage: $PROGNAME prepare|build|install|clean [opts]

Prepare options and their default values:

    ARCH=                The architecture to build for.
    CC=clang             The target compiler to use.
    CFLAGS=              The target CFLAGS to use.
    CROSS_COMPILE=       The cross triplet to use.
    CONFIG_FILE=         The config file to copy if not present.
    HOSTCC=clang         The host compiler to use.
    HOSTCFLAGS=          The host CFLAGS to use.
    LLVM=1               Use LLVM.
    LLVM_IAS=1           Use Clang integrated assembler.
    LD=lld               The linker to use.
    MAKE=gmake           The make to use.
    OBJDUMP=llvm-objdump The objdump binary to use.
    LOCALVERSION=        The CONFIG_LOCALVERSION to use.
    OBJDIR=build         The directory to build in.
    EPOCH=               The Unix timestamp for reproducible builds.
    JOBS=1               The number of build jobs to use.
    STRIP=1              Strip the modules.
    SPLIT_DBG=1          Separate the debug info.

Install target takes one argument, the destination directory.

Other commands do not take any arguments.

The build and clean stages need prepare to have run.
The install stage needs build to have run.

The program must be run within a kernel source tree.
}
EOF
}

die() {
    echo "ERROR: " $* 1>&2
    exit 1
}

COMMAND=$1

if [ -z "$COMMAND" ]; then
    usage 1>&2
    exit 1
fi

shift

# defaults

ARCH=$(uname -m)
CC=clang
CFLAGS=
CROSS_COMPILE=
CONFIG_FILE=
HOSTCC=clang
HOSTCFLAGS=
LLVM=1
LLVM_IAS=1
LD=lld
MAKE=gmake
OBJDUMP=llvm-objdump
LOCALVERSION=
OBJDIR=build
EPOCH=
JOBS=1
STRIP=1
SPLIT_DBG=1

case "$ARCH" in
    x86_64) ARCH=x86_64;;
    i?86) ARCH=i386;;
    arm*) ARCH=arm;;
    aarch64) ARCH=arm64;;
    ppc*) ARCH=powerpc;;
    riscv*) ARCH=riscv;;
    *) die "Unkonwn host architecture '$ARCH'";;
esac

validate_arch() {
    case "$ARCH" in
        x86_64|i386|arm|arm64|powerpc|riscv) ;;
        *) die "Unknown kernel architecture '$ARCH'";;
    esac
}

setup_epoch() {
    [ -z "$EPOCH" ] && return 0
    [ "$EPOCH" = "0" ] && return 0

    # reproducible builds
    export KBUILD_BUILD_TIMESTAMP=$(LC_ALL=C TZ=UTC date -jur "${EPOCH}")
    export KBUILD_BUILD_USER=chimera
    export KBUILD_BUILD_HOST=chimera
}

read_prepared() {
    local prepdir

    [ -r .chimera_prepare_done ] || die "Kernel tree not prepared."

    prepdir=$(cat .chimera_prepare_done)

    [ -d "$prepdir" ] || die "Configuration directory not found."

    ARCH=$(cat "${prepdir}/arch")
    CC=$(cat "${prepdir}/cc")
    CFLAGS=$(cat "${prepdir}/cflags")
    HOSTCC=$(cat "${prepdir}/hostcc")
    HOSTCFLAGS=$(cat "${prepdir}/hostcflags")
    [ -r "${prepdir}/cross" ] && CROSS_COMPILE=$(cat "${prepdir}/cross")
    LLVM=$(cat "${prepdir}/llvm")
    LLVM_IAS=$(cat "${prepdir}/llvm-ias")
    LD=$(cat "${prepdir}/ld")
    OBJDUMP=$(cat "${prepdir}/objdump")
    OBJDIR=$(cat "${prepdir}/objdir")
    JOBS=$(cat "${prepdir}/jobs")
    STRIP=$(cat "${prepdir}/strip")
    SPLIT_DBG=$(cat "${prepdir}/split-dbg")
    [ -r "${prepdir}/epoch" ] && EPOCH=$(cat "${prepdir}/epoch")

    export PATH="${prepdir}/wrappers:${PATH}"

    setup_epoch
}

call_make() {
    local cmdline

    objdump="$OBJDUMP"
    if [ "$objdump" != "llvm-objdump" ]; then
        objdump="${CROSS_COMPILE}${objdump}"
    fi
    cmdline="OBJDUMP=${objdump} LD=${CROSS_COMPILE}ld.${LD}"

    if [ $LLVM -ne 0 ]; then
        cmdline="$cmdline LLVM=1 LLVM_IAS=${LLVM_IAS}"
    fi

    if [ -n "$CROSS_COMPILE" ]; then
        cmdline="$cmdline CROSS_COMPILE=${CROSS_COMPILE}"
    fi

    env -u ARCH -u CC -u CFLAGS -u HOSTCC -u HOSTCFLAGS -u CROSS_COMPILE \
        -u LLVM -u LLVM_IAS -u LD -u OBJDUMP \
    ${MAKE} -j${JOBS} "O=${OBJDIR}" "$@" $cmdline ARCH=${ARCH} \
        "CC=${CC}" "HOSTCC=${HOSTCC}" \
        "CFLAGS=${CFLAGS}" \
        "HOSTCFLAGS=${HOSTCFLAGS}" \
            || die "Failed to run ${1}."
}

wrap_command() {
    local CMDPATH
    CMDPATH=$(command -v "$1")

    test $? -eq 0 || die "Command $1 does not exist."

    ln -sf "$CMDPATH" "$2" || die "Failed to wrap $1 as $2."
}

do_prepare() {
    local TEMPDIR

    [ ! -f Kconfig ] && die "$PROGNAME must be run inside a kernel tree."

    while [ $# -gt 0 ]; do
        case "$1" in
            ARCH=*) ARCH=${1#ARCH=};;
            CC=*) CC=${1#CC=};;
            CFLAGS=*) CFLAGS=${1#CFLAGS=};;
            CROSS_COMPILE=*) CROSS_COMPILE=${1#CROSS_COMPILE=};;
            CONFIG_FILE=*) CONFIG_FILE=${1#CONFIG_FILE=};;
            HOSTCC=*) HOSTCC=${1#HOSTCC=};;
            HOSTCFLAGS=*) HOSTCFLAGS=${1#HOSTCFLAGS=};;
            LLVM=*) LLVM=${1#LLVM=};;
            LLVM_IAS=*) LLVM_IAS=${1#LLVM_IAS=};;
            LD=*) LD=${1#LD=};;
            MAKE=*) MAKE=${1#MAKE=};;
            OBJDUMP=*) OBJDUMP=${1#OBJDUMP=};;
            LOCALVERSION=*) LOCALVERSION=${1#LOCALVERSION=};;
            OBJDIR=*) OBJDIR=${1#OBJDIR=};;
            EPOCH=*) EPOCH=${1#EPOCH=};;
            JOBS=*) JOBS=${1#JOBS=};;
            STRIP=*) STRIP=${1#STRIP=};;
            SPLIT_DBG=*) SPLIT_DBG=${1#SPLIT_DBG=};;
        esac
        shift
    done

    validate_arch
    setup_epoch

    rm -rf "${OBJDIR}" || die "Failed to remove build directory."
    mkdir -p "${OBJDIR}" || die "Failed to create build directory."

    [ -r "$CONFIG_FILE" ] || die "Config file is not readable."
    cp "$CONFIG_FILE" "${OBJDIR}/.config" \
        || die "Failed to copy config file."

    rm -f .chimera_prepare_done

    echo "=> Preparing wrappers..."

    TEMPDIR=$(mktemp -d "${OBJDIR}/chimera-kernel.XXXXXX")

    if [ $? -ne 0 ]; then
        die "Failed to create a settings directory."
    fi

    TEMPDIR=$(realpath "$TEMPDIR")

    if [ -n "$CROSS_COMPILE" ]; then
        CROSS_COMPILE="${CROSS_COMPILE}-"
    fi

    # prepare wrappers

    mkdir -p ${TEMPDIR}/wrappers

    wrap_command gfind ${TEMPDIR}/wrappers/find
    wrap_command gsed ${TEMPDIR}/wrappers/sed
    wrap_command gtar ${TEMPDIR}/wrappers/tar
    wrap_command ld.${LD} ${TEMPDIR}/wrappers/ld
    wrap_command ${MAKE} ${TEMPDIR}/wrappers/make
    wrap_command ${OBJDUMP} ${TEMPDIR}/wrappers/objdump

    if [ -n "$CROSS_COMPILE" ]; then
        if [ "$OBJDUMP" != "llvm-objdump" ]; then
            wrap_command ${CROSS_COMPILE}${OBJDUMP} \
                ${TEMPDIR}/wrappers/${CROSS_COMPILE}objdump
        fi
        if [ "$LD" != "lld" ]; then
            wrap_command ${CROSS_COMPILE}ld.${LD} \
                ${TEMPDIR}/wrappers/${CROSS_COMPILE}ld
        fi
        if [ $LLVM -ne 0 ]; then
            wrap_command clang ${TEMPDIR}/wrappers/${CROSS_COMPILE}clang
        fi
    fi

    export PATH="${TEMPDIR}/wrappers:${PATH}"

    echo "=> Preparing configuration..."

    # run oldconfig
    JOBS=1 call_make oldconfig

    # adjust localversion if needed
    if [ -n "$LOCALVERSION" ]; then
        gsed -i "s|^\(CONFIG_LOCALVERSION=\).*|\1\"${LOCALVERSION}\"|" ${OBJDIR}/.config
    fi

    echo "=> Preparing for build..."

    # run prepare
    call_make prepare

    # write things back out

    printf "%s" "$ARCH" > "${TEMPDIR}/arch"
    printf "%s" "$CC" > "${TEMPDIR}/cc"
    printf "%s" "$CFLAGS" > "${TEMPDIR}/cflags"
    printf "%s" "$HOSTCC" > "${TEMPDIR}/hostcc"
    printf "%s" "$HOSTCFLAGS" > "${TEMPDIR}/hostcflags"
    if [ -n "$CROSS_COMPILE" ]; then
        printf "%s" "$CROSS_COMPILE" > "${TEMPDIR}/cross"
    fi
    printf "%s" "$LLVM" > "${TEMPDIR}/llvm"
    printf "%s" "$LLVM_IAS" > "${TEMPDIR}/llvm-ias"
    printf "%s" "$LD" > "${TEMPDIR}/ld"
    printf "%s" "$OBJDUMP" > "${TEMPDIR}/objdump"
    printf "%s" "$OBJDIR" > "${TEMPDIR}/objdir"
    printf "%s" "$JOBS" > "${TEMPDIR}/jobs"
    printf "%s" "$EPOCH" > "${TEMPDIR}/epoch"
    printf "%s" "$STRIP" > "${TEMPDIR}/strip"
    printf "%s" "$SPLIT_DBG" > "${TEMPDIR}/split-dbg"

    printf "%s" "$TEMPDIR" > .chimera_prepare_done

    echo ""
    echo "Tree prepared, you can run build now."
}

do_config() {
    local tgt="$1"

    read_prepared

    if [ -z "$tgt" ]; then
        tgt="menuconfig"
    fi

    call_make "$tgt"
}

do_build() {
    local args
    local kernver

    read_prepared

    echo "=> Starting build..."

    case "$ARCH" in
        x86_64|i386) args="bzImage modules";;
        powerpc) args="zImage modules";;
        arm) args="zImage modules dtbs";;
        arm64|riscv) args="Image modules dtbs";;
    esac

    unset LDFLAGS
    call_make

    touch .chimera_build_done

    kernver=$(cat "${OBJDIR}/include/config/kernel.release")

    echo ""
    echo "Kernel build done ($kernver), you can run install now."
}

do_install() {
    local hdrdest
    local kernver
    local wrksrc

    read_prepared

    wrksrc=$(pwd)

    [ $# -eq 1 ] || die "Wrong arguments passed to install."
    [ -r .chimera_build_done ] || die "Kernel tree not built."

    kernver=$(cat "${OBJDIR}/include/config/kernel.release")

    DESTDIR="$1"

    mkdir -p "${DESTDIR}/usr/lib"
    # needed for depmod
    ln -sf usr/lib "${DESTDIR}/lib"

    [ -d "$DESTDIR" ] || die "Could not create destination directory."

    echo "=> Installing modules..."

    strip_exe=/usr/bin/true
    strip_arg=--strip-module

    if [ "$STRIP" -ne 0 ]; then
        strip_exe=/usr/bin/chimera-stripko
    fi
    if [ "$SPLIT_DBG" -ne 0 ]; then
        strip_arg="--strip-module=${DESTDIR}/usr/lib/debug"
    fi

    call_make modules_install INSTALL_MOD_PATH="$DESTDIR" \
        "MODLIB=${DESTDIR}/usr/lib/modules/${kernver}" \
        "STRIP=$strip_exe" "INSTALL_MOD_STRIP=$strip_arg"

    # can be renamed later
    hdrdest="${DESTDIR}/usr/src/linux-headers-${kernver}"

    echo "=> Installing kernel..."

    install -d "${DESTDIR}/boot"
    install -m644 "${OBJDIR}/.config" "${DESTDIR}/boot/config-${kernver}"
    install -m644 "${OBJDIR}/System.map" "${DESTDIR}/boot/System.map-${kernver}"

    case "$ARCH" in
        x86_64|i386)
            install -m 644 "${OBJDIR}/arch/x86/boot/bzImage" \
                "${DESTDIR}/boot/vmlinuz-${kernver}" \
                || die "failed to install kernel"
            ;;
        arm)
            install -m 644 "${OBJDIR}/arch/arm/boot/zImage" \
                "${DESTDIR}/boot/zImage-${kernver}" \
                || die "failed to install kernel"
            call_make dtbs_install \
                INSTALL_DTBS_PATH="${DESTDIR}/boot/dtbs/dtbs-${kernver}" \
                || die "failed to install dtbs"
            ;;
        arm64|riscv)
            install -m 644 "${OBJDIR}/arch/${ARCH}/boot/Image" \
                "${DESTDIR}/boot/vmlinux-${kernver}" \
                || die "failed to install kernel"
            call_make dtbs_install \
                INSTALL_DTBS_PATH="${DESTDIR}/boot/dtbs/dtbs-${kernver}" \
                || die "failed to install dtbs"
            ;;
        powerpc)
            install -m 644 "${OBJDIR}/vmlinux" \
                "${DESTDIR}/boot/vmlinux-${kernver}" \
                || die "failed to install kernel"
            /usr/bin/llvm-strip "${DESTDIR}/boot/vmlinux-${kernver}"
            ;;
    esac

    if [ "$SPLIT_DBG" -ne 0 ]; then
        install -d "${DESTDIR}/usr/lib/debug/boot"
        install -m644 "${OBJDIR}/vmlinux" \
            "${DESTDIR}/usr/lib/debug/boot/vmlinux-${kernver}"
    fi

    rm -f "${DESTDIR}/lib"

    cd "${DESTDIR}/usr/lib/modules/${kernver}" \
        || die "Could not change directory"

    rm -rf source build
    ln -sf "../../../src/linux-headers-${kernver}" build

    cd "${wrksrc}"

    echo "=> Setting up headers..."

    mkdir -p "${hdrdest}"

    # logic taken from Alpine

    cp "${DESTDIR}/boot/config-${kernver}" "${hdrdest}/.config"
    JOBS=1 OBJDIR="${hdrdest}" call_make \
        syncconfig prepare modules_prepare scripts

    rm -f "${hdrdest}/Makefile" "${hdrdest}/source"

    find . -path './include/*' -prune -o -path './scripts/*' -prune -o -type f \
        \( \
            -name 'Makefile*' -o -name 'Kconfig*' -o -name 'Kbuild*' -o \
            -name '*.sh' -o -name '*.pl' -o -name '*.lds' -o -name 'Platform' \
        \) -print | cpio -pdm "${hdrdest}"

    cp -a scripts include "${hdrdest}"

    find $(find arch -name include -type d -print) -type f \
        | cpio -pdm "${hdrdest}"

    install -m644 "${OBJDIR}/Module.symvers" "${hdrdest}"

    # crtsavres.o on powerpc with lld, needed for out of tree modules
    if [ -f "${OBJDIR}/arch/powerpc/lib/crtsavres.o" ]; then
        cp "${OBJDIR}/arch/powerpc/lib/crtsavres.o" \
            "${hdrdest}/arch/powerpc/lib"
    fi

    echo ""
    echo "Kernel installation done ($kernver), files in ${DESTDIR}."
}

do_clean() {
    read_prepared

    echo "=> Cleaning kernel tree..."

    call_make mrproper

    rm -rf .chimera* 2>/dev/null
    rm -rf "${OBJDIR}" 2>/dev/null
}

case $COMMAND in
    prepare) do_prepare "$@";;
    config) do_config "$@";;
    build) do_build;;
    install) do_install "$@";;
    clean) do_clean;;
    *)
        echo "Unknown command: $COMMAND" 1>&2
        echo "" 1>&2
        usage 1>&2
        exit 1
        ;;
esac
