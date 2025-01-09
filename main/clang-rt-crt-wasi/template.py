pkgname = "clang-rt-crt-wasi"
pkgver = "19.1.6"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DCMAKE_BUILD_TYPE=Release",
    "-DCMAKE_SYSTEM_NAME=WASI",
    "-DCMAKE_SYSTEM_VERSION=1",
    "-DCMAKE_SYSTEM_PROCESSOR=wasm32",
    "-DCMAKE_SYSROOT=/usr/wasm32-unknown-wasi",
    f"-DCMAKE_INSTALL_PREFIX=/usr/lib/clang/{pkgver[0 : pkgver.find('.')]}",
    # prevent executable checks
    "-DCMAKE_TRY_COMPILE_TARGET_TYPE=STATIC_LIBRARY",
    # only build that target
    "-DCOMPILER_RT_DEFAULT_TARGET_ONLY=ON",
    # tools
    "-DCMAKE_C_COMPILER=/usr/bin/clang",
    "-DCMAKE_ASM_COMPILER_TARGET=wasm32-unknown-wasi",
    "-DCMAKE_C_COMPILER_TARGET=wasm32-unknown-wasi",
    "-DCMAKE_CXX_COMPILER_TARGET=wasm32-unknown-wasi",
    "-DCMAKE_C_FLAGS=-O2",
    "-DCMAKE_CXX_FLAGS=-O2",
    "-DCMAKE_AR=/usr/bin/llvm-ar",
    "-DCMAKE_NM=/usr/bin/llvm-nm",
    "-DCMAKE_RANLIB=/usr/bin/llvm-ranlib",
    "-DLLVM_CONFIG_PATH=/usr/bin/llvm-config",
    "-DCOMPILER_RT_BAREMETAL_BUILD=ON",
    "-DCOMPILER_RT_HAS_FPIC_FLAG=OFF",
    "-DCOMPILER_RT_OS_DIR=wasi",
]
cmake_dir = "compiler-rt"
hostmakedepends = [
    "clang-tools-extra",
    "cmake",
    "llvm-devel",
    "ninja",
    "python",
    "wasi-libc",
]
depends = ["wasi-libc"]
pkgdesc = "Compiler runtime for WASI"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0 WITH LLVM-exception AND NCSA"
url = "https://llvm.org"
source = f"https://github.com/llvm/llvm-project/releases/download/llvmorg-{pkgver}/llvm-project-{pkgver}.src.tar.xz"
sha256 = "e3f79317adaa9196d2cfffe1c869d7c100b7540832bc44fe0d3f44a12861fa34"
debug_level = 0
hardening = ["!int", "!scp", "!var-init"]
# crosstoolchain
options = ["!cross", "!check", "!lto", "!strip"]


def post_patch(self):
    self.mkdir("compiler-rt/cmake/Platform")
    with open(self.cwd / "compiler-rt/cmake/Platform/WASI.cmake", "w") as outf:
        outf.write("set(WASI 1)\n")


def init_configure(self):
    self.configure_args.append(
        f"-DCMAKE_MODULE_PATH={self.chroot_cwd}/compiler-rt/cmake"
    )


def post_install(self):
    self.install_license("LICENSE.TXT")
    self.uninstall(f"usr/lib/clang/{pkgver[0 : pkgver.find('.')]}/include")
    self.install_link(
        f"usr/lib/clang/{pkgver[0 : pkgver.find('.')]}/lib/wasip1", "wasi"
    )
    self.install_link(
        f"usr/lib/clang/{pkgver[0 : pkgver.find('.')]}/lib/wasip2", "wasi"
    )
