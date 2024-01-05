pkgname = "libcxx-wasi"
pkgver = "17.0.6"
pkgrel = 1
build_style = "cmake"
configure_args = [
    "-DCMAKE_BUILD_TYPE=Release",
    "-DCMAKE_SYSTEM_NAME=WASI",
    "-DCMAKE_SYSTEM_VERSION=1",
    "-DCMAKE_SYSTEM_PROCESSOR=wasm32",
    "-Wno-dev",
    "-DCMAKE_SYSROOT=/usr/wasm32-unknown-wasi",
    "-DCMAKE_INSTALL_PREFIX=/",
    # prevent executable checks
    "-DCMAKE_TRY_COMPILE_TARGET_TYPE=STATIC_LIBRARY",
    # tools
    "-DCMAKE_C_COMPILER=/usr/bin/clang",
    "-DCMAKE_C_COMPILER_WORKS=ON",
    "-DCMAKE_CXX_COMPILER_WORKS=ON",
    "-DCMAKE_ASM_COMPILER_WORKS=ON",
    "-DLIBCXXABI_USE_COMPILER_RT=YES",
    "-DLIBCXXABI_ENABLE_SHARED=OFF",
    "-DLIBCXXABI_ENABLE_EXCEPTIONS=OFF",
    "-DLIBCXXABI_HAS_EXTERNAL_THREAD_API=OFF",
    "-DLIBCXXABI_HAS_WIN32_THREAD_API=OFF",
    "-DLIBCXXABI_SILENT_TERMINATE=ON",
    "-DLIBCXX_USE_COMPILER_RT=YES",
    "-DLIBCXX_HAS_MUSL_LIBC=ON",
    "-DLIBCXX_CXX_ABI=libcxxabi",
    "-DLIBCXX_ENABLE_STATIC_ABI_LIBRARY=NO",
    "-DLIBCXX_ENABLE_EXCEPTIONS=NO",
    "-DLIBCXX_ENABLE_FILESYSTEM=NO",
    "-DLIBCXX_ENABLE_SHARED=NO",
    "-DLIBCXX_HAS_EXTERNAL_THREAD_API=OFF",
    "-DLIBCXX_HARDENING_MODE=hardened",
    "-DLLVM_ENABLE_RUNTIMES=libcxxabi;libcxx",
    "-DCMAKE_AR=/usr/bin/llvm-ar",
    "-DCMAKE_NM=/usr/bin/llvm-nm",
    "-DCMAKE_RANLIB=/usr/bin/llvm-ranlib",
    "-DUNIX=ON",
]
make_cmd = "make"
cmake_dir = "runtimes"
hostmakedepends = [
    "clang-tools-extra",
    "cmake",
    "python",
    "llvm-devel",
    "wasi-libc",
    "clang-rt-crt-wasi",
]
depends = [f"clang-rt-crt-wasi~{pkgver}"]
pkgdesc = "Compiler runtime for WASI"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://llvm.org"
source = f"https://github.com/llvm/llvm-project/releases/download/llvmorg-{pkgver}/llvm-project-{pkgver}.src.tar.xz"
sha256 = "58a8818c60e6627064f312dbf46c02d9949956558340938b71cf731ad8bc0813"
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


def do_configure(self):
    from cbuild.util import cmake

    with self.stamp("nothread_configure") as s:
        s.check()
        cmake.configure(
            self,
            "build-nothread",
            self.cmake_dir,
            configure_args
            + [
                "-DCMAKE_ASM_COMPILER_TARGET=wasm32-unknown-wasi",
                "-DCMAKE_C_COMPILER_TARGET=wasm32-unknown-wasi",
                "-DCMAKE_CXX_COMPILER_TARGET=wasm32-unknown-wasi",
                "-DCMAKE_C_FLAGS=-O2",
                "-DCMAKE_CXX_FLAGS=-O2",
                "-DLIBCXXABI_ENABLE_THREADS=OFF",
                "-DLIBCXXABI_HAS_PTHREAD_API=OFF",
                "-DLIBCXX_ENABLE_THREADS=OFF",
                "-DLIBCXX_HAS_PTHREAD_API=OFF",
                "-DLIBCXX_LIBDIR_SUFFIX=/wasm32-wasi",
                # this is necessary! the config headers record the overall
                # configuration which will differ if threads are enabled
                "-DLIBCXX_INSTALL_INCLUDE_DIR=include/wasm32-wasi/c++/v1",
                "-DLIBCXX_INSTALL_INCLUDE_TARGET_DIR=include/wasm32-wasi/c++/v1",
                "-DLIBCXXABI_LIBDIR_SUFFIX=/wasm32-wasi",
                "-DLIBCXXABI_INSTALL_INCLUDE_DIR=include/wasm32-wasi/c++/v1",
            ],
            cross_build=False,
            generator="Unix Makefiles",
        )
    with self.stamp("thread_configure") as s:
        s.check()
        cmake.configure(
            self,
            "build-thread",
            self.cmake_dir,
            configure_args
            + [
                "-DCMAKE_ASM_COMPILER_TARGET=wasm32-unknown-wasi-threads",
                "-DCMAKE_C_COMPILER_TARGET=wasm32-unknown-wasi-threads",
                "-DCMAKE_CXX_COMPILER_TARGET=wasm32-unknown-wasi-threads",
                "-DCMAKE_C_FLAGS=-O2 -pthread",
                "-DCMAKE_CXX_FLAGS=-O2 -pthread",
                "-DLIBCXXABI_ENABLE_THREADS=ON",
                "-DLIBCXXABI_HAS_PTHREAD_API=ON",
                "-DLIBCXX_ENABLE_THREADS=ON",
                "-DLIBCXX_HAS_PTHREAD_API=ON",
                "-DLIBCXX_LIBDIR_SUFFIX=/wasm32-wasi-threads",
                "-DLIBCXX_INSTALL_INCLUDE_DIR=include/wasm32-wasi-threads/c++/v1",
                "-DLIBCXX_INSTALL_INCLUDE_TARGET_DIR=include/wasm32-wasi-threads/c++/v1",
                "-DLIBCXXABI_LIBDIR_SUFFIX=/wasm32-wasi-threads",
                "-DLIBCXXABI_INSTALL_INCLUDE_DIR=include/wasm32-wasi-threads/c++/v1",
            ],
            cross_build=False,
            generator="Unix Makefiles",
        )


def do_build(self):
    from cbuild.util import cmake

    with self.stamp("nothread_build") as s:
        s.check()
        cmake.build(self, "build-nothread")

    with self.stamp("thread_build") as s:
        s.check()
        cmake.build(self, "build-thread")


def do_install(self):
    from cbuild.util import cmake

    with self.stamp("nothread_install") as s:
        s.check()
        cmake.install(
            self,
            "build-nothread",
            env={
                "DESTDIR": str(self.chroot_destdir / "usr/wasm32-unknown-wasi")
            },
        )

    with self.stamp("thread_install") as s:
        s.check()
        cmake.install(
            self,
            "build-thread",
            env={
                "DESTDIR": str(self.chroot_destdir / "usr/wasm32-unknown-wasi")
            },
        )

    # clang will not try including any c++ paths unless this path exists
    self.install_dir("usr/wasm32-unknown-wasi/include/c++/v1")
    (self.destdir / "usr/wasm32-unknown-wasi/include/c++/v1/__empty").touch()
