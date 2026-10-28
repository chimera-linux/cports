#!/bin/sh
## Credit to @Martchus
## Based on https://github.com/Martchus/PKGBUILDs/blob/a7036fac2108701dab2afa277d5d8eade63b708c/environment/mingw-w64-clang/mingw-env.sh

if [ -z "${_mingw_arch}" ]; then
	echo "Error: "\${_mingw_arch}" has to be set by caller of this script" >&2
	exit 1
fi

_arch_="${_mingw_arch%%-*}"
arch_flags=""
#[ "${_arch_}" == aarch64 ] && arch_flags="-march=armv8.1-a"
[ "${_arch_}" = x86_64 ] && arch_flags="-march=nocona -msahf -mtune=generic"

cross_clang_flags="-rtlib=compiler-rt -fuse-ld=lld -target ${_mingw_arch} -Xclang -triple -Xclang ${_mingw_arch}"

# omit `-Wp,-D_FORTIFY_SOURCE=2` for now as it causes Qt 6 apps to hang, see f7c5947c2c92f516701d40373c98af3556edf8f6
# and https://github.com/msys2/MINGW-packages/pull/31309#issuecomment-5505514064
# TODO try with those flags on. probably ok since we have musl-libssp-static 
default_mingw_pp_flags=""

default_mingw_compiler_flags="$cross_clang_flags $default_mingw_pp_flags $arch_flags -O2 -pipe -fexceptions -fstack-protector-strong -Wformat -Werror=format-security"
default_mingw_cxx_compiler_flags="$default_mingw_compiler_flags"
default_mingw_linker_flags="$cross_clang_flags -Wl,-O1,--sort-common,--as-needed"

# do NOT enable `-mguard=cf` and `-fcf-protection` by default in consistency with MSYS2 packages
if [ -n "$USE_FC_PROTECTION" ] && [ "${_arch_}" != aarch64 ] && [ "${_arch_}" != armv7 ];then
	default_mingw_compiler_flags="${default_mingw_compiler_flags} -fcf-protection"
fi
if [ -n "$USE_MGUARD" ]; then
	default_mingw_compiler_flags="${default_mingw_compiler_flags} -mguard=cf"
fi

export MINGW_W64_CLANG_TARGET="${_mingw_arch}"
export CPPFLAGS="${MINGW_CPPFLAGS:-$default_mingw_pp_flags $CPPFLAGS}"
export CFLAGS="${MINGW_CFLAGS:-$default_mingw_compiler_flags $CFLAGS}"
export CXXFLAGS="${MINGW_CXXFLAGS:-$default_mingw_cxx_compiler_flags $CXXFLAGS}"
export ASMFLAGS="${MINGW_ASMFLAGS:-$default_mingw_compiler_flags $ASMFLAGS}"
export LDFLAGS="${MINGW_LDFLAGS:-$default_mingw_linker_flags $LDFLAGS}"

export CC="${MINGW_CC:-${_mingw_arch}-clang}"
export CXX="${MINGW_CXX:-${_mingw_arch}-clang++}"
export ASM="${MINGW_ASM:-${_mingw_arch}-clang}"
export AR="${MINGW_AR:-llvm-ar}"
export NM="${MINGW_NM:-llvm-nm}"
export LD="${MINGW_LD:-lld}"
export STRIP="${MINGW_STRIP:-llvm-strip}"
export RANLIB="${MINGW_RANLIB:-llvm-ranlib}"
export DLLTOOL="${MINGW_DLLTOOL:-llvm-dlltool}"
export WINDRES="${MINGW_WINDRES:-llvm-windres}"
export RC="${MINGW_RC:-llvm-windres}"

_mingw_prefix=/usr/"${_mingw_arch}"
export PKG_CONFIG_SYSROOT_DIR="${_mingw_prefix}"
export PKG_CONFIG_LIBDIR="${mingw_prefix}/lib/pkgconfig:${mingw_prefix}/share/pkgconfig"
