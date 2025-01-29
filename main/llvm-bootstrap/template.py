pkgname = "llvm-bootstrap"
pkgver = "19.1.7"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DCMAKE_BUILD_TYPE=Release",
    "-DCMAKE_INSTALL_PREFIX=/usr/lib/llvm-bootstrap",
    # use rpath so the installed tools always use their own libs
    "-DCMAKE_INSTALL_RPATH=/usr/lib/llvm-bootstrap/lib",
    # in sync with main/llvm
    "-DENABLE_LINKER_BUILD_ID=ON",
    "-DCOMPILER_RT_USE_BUILTINS_LIBRARY=ON",
    "-DLIBCXX_CXX_ABI=libcxxabi",
    "-DLIBCXX_USE_COMPILER_RT=ON",
    "-DLIBCXX_ENABLE_STATIC_ABI_LIBRARY=OFF",
    "-DLIBCXX_HAS_MUSL_LIBC=ON",
    "-DLIBCXX_HARDENING_MODE=fast",
    "-DLIBCXXABI_USE_LLVM_UNWINDER=ON",
    "-DLIBCXXABI_ENABLE_STATIC_UNWINDER=OFF",
    "-DLIBCXXABI_USE_COMPILER_RT=ON",
    "-DLLVM_INSTALL_UTILS=ON",
    "-DLLVM_BUILD_LLVM_DYLIB=ON",
    "-DLLVM_LINK_LLVM_DYLIB=ON",
    "-DLLVM_ENABLE_RTTI=ON",
    "-DLLVM_ENABLE_PER_TARGET_RUNTIME_DIR=ON",
    "-DCLANG_DEFAULT_RTLIB=compiler-rt",
    "-DCLANG_DEFAULT_UNWINDLIB=libunwind",
    "-DCLANG_DEFAULT_CXX_STDLIB=libc++",
    "-DCLANG_CONFIG_FILE_SYSTEM_DIR=/etc/clang",
    "-DLLVM_ENABLE_LLD=ON",
    "-DLLVM_ENABLE_LIBCXX=ON",
    "-DLIBUNWIND_USE_COMPILER_RT=ON",
    # disable all the stuff we don't want and enable only some components
    "-DLLVM_ENABLE_LIBXML2=OFF",
    "-DLLVM_ENABLE_LIBEDIT=OFF",
    "-DLLVM_ENABLE_LIBPFM=OFF",
    "-DCOMPILER_RT_BUILD_SANITIZERS=OFF",
    "-DCOMPILER_RT_BUILD_XRAY=OFF",
    "-DCOMPILER_RT_BUILD_LIBFUZZER=OFF",
    "-DCOMPILER_RT_BUILD_PROFILE=OFF",
    "-DCOMPILER_RT_BUILD_MEMPROF=OFF",
    "-DCOMPILER_RT_BUILD_CTX_PROFILE=OFF",
    # only build that target
    "-DCOMPILER_RT_DEFAULT_TARGET_ONLY=ON",
    "-DLLVM_ENABLE_PROJECTS=clang;lld",
    "-DLLVM_ENABLE_RUNTIMES=compiler-rt;libcxx;libcxxabi;libunwind",
]
hostmakedepends = ["cmake", "ninja", "pkgconf", "perl", "python"]
makedepends = [
    "zlib-ng-compat-devel",
    "libatomic-chimera-devel",
    "linux-headers",
]
depends = ["fortify-headers", "libatomic-chimera-devel"]
pkgdesc = "Low Level Virtual Machine"
subdesc = "bootstrap"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0 WITH LLVM-exception AND NCSA"
url = "https://llvm.org"
source = f"https://github.com/llvm/llvm-project/releases/download/llvmorg-{pkgver}/llvm-project-{pkgver}.src.tar.xz"
sha256 = "82401fea7b79d0078043f7598b835284d6650a75b93e64b6f761ea7b63097501"
debug_level = 0
# see llvm template
hardening = ["!int"]
# bootstrap; LTO would just slow it down, cross is unnecessary (not used
# in cross builds), debug info is unnecessary, and dependency/shlib scan
# would be actually harmful
# runtimes build may invoke built clang during install, which has
# rpath and fakeroot effectively overrides rpath, so disable that
options = [
    "!lto",
    "!cross",
    "!check",
    "!debug",
    "!installroot",
    "!scanshlibs",
    "!scanrundeps",
    "!autosplit",
]

cmake_dir = "llvm"

tool_flags = {
    "CFLAGS": ["-fPIC"],
    "CXXFLAGS": ["-fPIC"],
}

match self.profile().arch:
    case "x86_64":
        _arch = "X86"
    case "aarch64":
        _arch = "AArch64"
    case "ppc64le" | "ppc64" | "ppc":
        _arch = "PowerPC"
    case "riscv64":
        _arch = "RISCV64"
    case "loongarch64" | "loongarch32":
        _arch = "LoongArch"
    case _:
        _arch = ""
        broken = f"Unknown CPU architecture: {self.profile().arch}"

configure_args += [
    "-DLLVM_TARGET_ARCH=" + _arch,
    "-DLLVM_HOST_TRIPLE=" + self.profile().triplet,
    "-DLLVM_DEFAULT_TARGET_TRIPLE=" + self.profile().triplet,
]


def post_install(self):
    self.install_license("LICENSE.TXT")
    # otherwise it'd use /usr/bin/ld by default
    self.install_link("usr/lib/llvm-bootstrap/bin/ld", "ld.lld")
    # cc/c++ symlinks
    self.install_link("usr/lib/llvm-bootstrap/bin/cc", "clang")
    self.install_link("usr/lib/llvm-bootstrap/bin/c++", "clang++")
