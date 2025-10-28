pkgname = "clang-rt-crt-wasi"
pkgver = "21.1.4"
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
    "-DCOMPILER_RT_BUILD_LIBFUZZER=OFF",
    "-DCOMPILER_RT_BUILD_MEMPROF=OFF",
    "-DCOMPILER_RT_BUILD_PROFILE=OFF",
    "-DCOMPILER_RT_BUILD_SANITIZERS=OFF",
    "-DCOMPILER_RT_BUILD_XRAY=OFF",
    "-DCOMPILER_RT_BUILD_ORC=OFF",
    "-DCOMPILER_RT_BUILD_CTX_PROFILE=OFF",
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
license = "Apache-2.0 WITH LLVM-exception AND NCSA"
url = "https://llvm.org"
source = f"https://github.com/llvm/llvm-project/releases/download/llvmorg-{pkgver}/llvm-project-{pkgver}.src.tar.xz"
sha256 = "a01ad7e5167780c945871d75c0413081d12067607a6de5cf71dc3e8d1a82112c"
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
    self.install_link(
        f"usr/lib/clang/{pkgver[0 : pkgver.find('.')]}/lib/wasip1", "wasi"
    )
    self.install_link(
        f"usr/lib/clang/{pkgver[0 : pkgver.find('.')]}/lib/wasip2", "wasi"
    )
