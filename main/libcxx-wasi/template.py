pkgname = "libcxx-wasi"
pkgver = "21.1.8"
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
    "-DCMAKE_C_COMPILER=/usr/bin/clang",
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
    "-DCMAKE_AR=/usr/bin/llvm-ar",
    "-DCMAKE_NM=/usr/bin/llvm-nm",
    "-DCMAKE_RANLIB=/usr/bin/llvm-ranlib",
    "-DUNIX=ON",
]
cmake_dir = "runtimes"
hostmakedepends = [
    "clang-devel",
    "clang-rt-crt-wasi",
    "clang-tools-extra",
    "cmake",
    "llvm-devel",
    "ninja",
    "python",
    "wasi-libc",
]
depends = [f"clang-rt-crt-wasi~{pkgver}"]
pkgdesc = "Compiler runtime for WASI"
license = "Apache-2.0 WITH LLVM-exception AND NCSA"
url = "https://llvm.org"
source = f"https://github.com/llvm/llvm-project/releases/download/llvmorg-{pkgver}/llvm-project-{pkgver}.src.tar.xz"
sha256 = "4633a23617fa31a3ea51242586ea7fb1da7140e426bd62fc164261fe036aa142"
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
