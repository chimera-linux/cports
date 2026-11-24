pkgname = "llvm23-runtimes-wasi"
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
    "-DCMAKE_STAGING_PREFIX=/usr/wasm32-unknown-wasi",
    # prevent executable checks
    "-DCMAKE_TRY_COMPILE_TARGET_TYPE=STATIC_LIBRARY",
    # tools
    f"-DCMAKE_C_COMPILER=/usr/bin/clang-{_llvm_majver}",
    "-DCMAKE_C_COMPILER_WORKS=ON",
    "-DCMAKE_CXX_COMPILER_WORKS=ON",
    "-DCMAKE_ASM_COMPILER_WORKS=ON",
    "-DLIBCXXABI_USE_COMPILER_RT=ON",
    "-DLIBCXXABI_USE_LLVM_UNWINDER=OFF",
    "-DLIBCXXABI_ENABLE_SHARED=OFF",
    "-DLIBCXXABI_ENABLE_EXCEPTIONS=OFF",
    "-DLIBCXXABI_HAS_EXTERNAL_THREAD_API=OFF",
    "-DLIBCXXABI_HAS_WIN32_THREAD_API=OFF",
    "-DLIBCXXABI_SILENT_TERMINATE=ON",
    "-DLIBCXX_USE_COMPILER_RT=ON",
    "-DLIBCXX_HAS_MUSL_LIBC=ON",
    "-DLIBCXX_CXX_ABI=libcxxabi",
    "-DLIBCXX_ENABLE_STATIC_ABI_LIBRARY=OFF",
    "-DLIBCXX_ENABLE_EXCEPTIONS=OFF",
    "-DLIBCXX_ENABLE_FILESYSTEM=OFF",
    "-DLIBCXX_ENABLE_SHARED=OFF",
    "-DLIBCXX_HAS_EXTERNAL_THREAD_API=OFF",
    "-DLIBCXX_HARDENING_MODE=fast",
    "-DLLVM_ENABLE_PER_TARGET_RUNTIME_DIR=ON",
    "-DLLVM_ENABLE_RUNTIMES=libcxxabi;libcxx",
    f"-DCMAKE_AR=/usr/bin/llvm-ar-{_llvm_majver}",
    f"-DCMAKE_NM=/usr/bin/llvm-nm-{_llvm_majver}",
    f"-DCMAKE_RANLIB=/usr/bin/llvm-ranlib-{_llvm_majver}",
    "-DUNIX=ON",
]
cmake_dir = "runtimes"
hostmakedepends = [
    "cmake",
    f"llvm{_llvm_majver}-clang-rt-crt-wasi",
    f"llvm{_llvm_majver}-clang-devel",
    f"llvm{_llvm_majver}-devel",
    "ninja",
    "python",
    "wasi-libc",
]
depends = [f"llvm{_llvm_majver}-clang-rt-crt-wasi~{pkgver}"]
# transitional old name + new generic name as we can only have one of this
renames = ["libcxx-wasi", "llvm-runtimes-wasi"]
pkgdesc = "Compiler runtime for WASI"
license = "Apache-2.0 WITH LLVM-exception AND NCSA"
url = "https://llvm.org"
source = f"https://github.com/llvm/llvm-project/releases/download/llvmorg-{pkgver}/llvm-project-{pkgver}.src.tar.xz"
sha256 = "d3b86ab29cfb4445a6652e5c2642ccc75e04e38084dde3701d323320f35a31da"
hardening = ["!int", "!scp", "!var-init"]
# crosstoolchain
options = ["!cross", "!check", "!lto", "!strip"]


_targets = [
    ("wasm32-wasip1", False),
    ("wasm32-wasip1-threads", True),
    ("wasm32-wasip2", False),
]


def post_patch(self):
    self.mkdir("compiler-rt/cmake/Platform")
    with open(self.cwd / "compiler-rt/cmake/Platform/WASI.cmake", "w") as outf:
        outf.write("set(WASI 1)\n")


def init_configure(self):
    self.configure_args.append(
        f"-DCMAKE_MODULE_PATH={self.chroot_cwd}/compiler-rt/cmake"
    )


def configure(self):
    from cbuild.util import cmake

    for tgt in _targets:
        with self.stamp(f"{tgt[0]}_configure") as s:
            s.check()
            threads = "ON" if tgt[1] else "OFF"
            flags = "-O2 -pthread" if tgt[1] else "-O2"
            cmake.configure(
                self,
                f"build-{tgt[0]}",
                self.cmake_dir,
                [
                    *configure_args,
                    f"-DCMAKE_ASM_COMPILER_TARGET={tgt[0]}",
                    f"-DCMAKE_C_COMPILER_TARGET={tgt[0]}",
                    f"-DCMAKE_CXX_COMPILER_TARGET={tgt[0]}",
                    f"-DCMAKE_C_FLAGS={flags}",
                    f"-DCMAKE_CXX_FLAGS={flags}",
                    f"-DLLVM_DEFAULT_TARGET_TRIPLE={tgt[0]}",
                    f"-DLIBCXXABI_ENABLE_THREADS={threads}",
                    f"-DLIBCXXABI_HAS_PTHREAD_API={threads}",
                    f"-DLIBCXX_ENABLE_THREADS={threads}",
                    f"-DLIBCXX_HAS_PTHREAD_API={threads}",
                    # this is necessary! the config headers record the overall
                    # configuration which will differ if threads are enabled
                    f"-DLIBCXX_INSTALL_INCLUDE_DIR=include/{tgt[0]}/c++/v1",
                    f"-DLIBCXX_INSTALL_INCLUDE_TARGET_DIR=include/{tgt[0]}/c++/v1",
                    f"-DLIBCXXABI_INSTALL_INCLUDE_DIR=include/{tgt[0]}/c++/v1",
                ],
                cross_build=False,
            )


def build(self):
    from cbuild.util import cmake

    for tgt in _targets:
        with self.stamp(f"{tgt[0]}_build") as s:
            s.check()
            cmake.build(self, f"build-{tgt[0]}")


def install(self):
    from cbuild.util import cmake

    for tgt in _targets:
        cmake.install(self, f"build-{tgt[0]}")

    self.install_license("LICENSE.TXT")

    # clang will not try including any c++ paths unless this path exists
    self.install_dir("usr/wasm32-unknown-wasi/include/c++/v1")
    (self.destdir / "usr/wasm32-unknown-wasi/include/c++/v1/__empty").touch()

    # rename wrong dirs...
    self.rename(
        "usr/wasm32-unknown-wasi/lib/wasm32-unknown-wasip1", "wasm32-wasip1"
    )
    self.rename(
        "usr/wasm32-unknown-wasi/lib/wasm32-unknown-wasip1-threads",
        "wasm32-wasip1-threads",
    )
    self.rename(
        "usr/wasm32-unknown-wasi/lib/wasm32-unknown-wasip2", "wasm32-wasip2"
    )
