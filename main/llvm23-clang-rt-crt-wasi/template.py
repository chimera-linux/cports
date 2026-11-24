pkgname = "llvm23-clang-rt-crt-wasi"
pkgver = "23.1.6"
_llvm_majver = pkgver[0:2]
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DCMAKE_BUILD_TYPE=Release",
    "-DCMAKE_SYSTEM_NAME=WASI",
    "-DCMAKE_SYSTEM_VERSION=1",
    "-DCMAKE_SYSTEM_PROCESSOR=wasm32",
    "-DCMAKE_SYSROOT=/usr/wasm32-unknown-wasi",
    f"-DCMAKE_INSTALL_PREFIX=/usr/lib/llvm{_llvm_majver}/lib/clang/{_llvm_majver}",
    # prevent executable checks
    "-DCMAKE_TRY_COMPILE_TARGET_TYPE=STATIC_LIBRARY",
    # only build that target
    "-DCOMPILER_RT_DEFAULT_TARGET_ONLY=ON",
    # tools
    f"-DCMAKE_C_COMPILER=/usr/bin/clang-{_llvm_majver}",
    "-DCMAKE_ASM_COMPILER_TARGET=wasm32-unknown-wasi",
    "-DCMAKE_C_COMPILER_TARGET=wasm32-unknown-wasi",
    "-DCMAKE_CXX_COMPILER_TARGET=wasm32-unknown-wasi",
    "-DCMAKE_C_FLAGS=-O2",
    "-DCMAKE_CXX_FLAGS=-O2",
    f"-DCMAKE_AR=/usr/bin/llvm-ar-{_llvm_majver}",
    f"-DCMAKE_NM=/usr/bin/llvm-nm-{_llvm_majver}",
    f"-DCMAKE_RANLIB=/usr/bin/llvm-ranlib-{_llvm_majver}",
    f"-DLLVM_CONFIG_PATH=/usr/bin/llvm-config-{_llvm_majver}",
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
    "cmake",
    f"llvm{_llvm_majver}-devel",
    "ninja",
    "python",
    "wasi-libc",
]
depends = [f"llvm{_llvm_majver}-clang", "wasi-libc"]
pkgdesc = "Compiler runtime for WASI"
license = "Apache-2.0 WITH LLVM-exception AND NCSA"
url = "https://llvm.org"
source = f"https://github.com/llvm/llvm-project/releases/download/llvmorg-{pkgver}/llvm-project-{pkgver}.src.tar.xz"
sha256 = "d3b86ab29cfb4445a6652e5c2642ccc75e04e38084dde3701d323320f35a31da"
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
        f"usr/lib/llvm{_llvm_majver}/lib/clang/{_llvm_majver}/lib/wasip1",
        "wasi",
    )
    self.install_link(
        f"usr/lib/llvm{_llvm_majver}/lib/clang/{_llvm_majver}/lib/wasip2",
        "wasi",
    )
