pkgname = "clang-rt-crt-wasi"
pkgver = "18.1.8"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DCMAKE_BUILD_TYPE=Release",
    "-DCMAKE_SYSTEM_NAME=WASI",
    "-DCMAKE_SYSTEM_VERSION=1",
    "-DCMAKE_SYSTEM_PROCESSOR=wasm32",
    "-DCMAKE_SYSROOT=/usr/wasm32-unknown-wasi",
    f"-DCMAKE_INSTALL_PREFIX=/usr/lib/clang/{pkgver[0:pkgver.find('.')]}",
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
make_cmd = "make"
cmake_dir = "compiler-rt"
hostmakedepends = [
    "clang-tools-extra",
    "cmake",
    "python",
    "llvm-devel",
    "wasi-libc",
]
depends = ["wasi-libc"]
pkgdesc = "Compiler runtime for WASI"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://llvm.org"
source = f"https://github.com/llvm/llvm-project/releases/download/llvmorg-{pkgver}/llvm-project-{pkgver}.src.tar.xz"
sha256 = "0b58557a6d32ceee97c8d533a59b9212d87e0fc4d2833924eb6c611247db2f2a"
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
    self.uninstall(f"usr/lib/clang/{pkgver[0:pkgver.find('.')]}/include")
