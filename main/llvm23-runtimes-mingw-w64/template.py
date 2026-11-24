pkgname = "llvm23-runtimes-mingw-w64"
pkgver = "23.1.6"
_llvm_majver = pkgver[0:2]
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DCMAKE_SYSTEM_NAME=Windows",
    "-DCMAKE_BUILD_TYPE=Release",
    f"-DCMAKE_C_COMPILER=/usr/bin/clang-{_llvm_majver}",
    f"-DCMAKE_CXX_COMPILER=/usr/bin/clang++-{_llvm_majver}",
    f"-DCMAKE_AR=/usr/bin/llvm-ar-{_llvm_majver}",
    f"-DCMAKE_NM=/usr/bin/llvm-nm-{_llvm_majver}",
    f"-DCMAKE_RANLIB=/usr/bin/llvm-ranlib-{_llvm_majver}",
    f"-DLLVM_CONFIG_PATH=/usr/bin/llvm-config-{_llvm_majver}",
    # prevent executable checks
    "-DCMAKE_TRY_COMPILE_TARGET_TYPE=STATIC_LIBRARY",
    # build these runtimes
    "-DLLVM_ENABLE_RUNTIMES=libcxx;libcxxabi;libunwind",
    # don't use libgcc
    "-DLIBUNWIND_USE_COMPILER_RT=ON",
    "-DLIBCXX_USE_COMPILER_RT=ON",
    "-DLIBCXXABI_USE_COMPILER_RT=ON",
    # FIXME: undefined symbols
    "-DLIBCXXABI_ENABLE_SHARED=OFF",
    # ensures we don't need to link libc++abi manually
    "-DLIBCXX_ENABLE_STATIC_ABI_LIBRARY=ON",
    # helps split up target-agnostic from target-specific files
    "-DLLVM_ENABLE_PER_TARGET_RUNTIME_DIR=ON",
    # tries to link to -ldl otherwise
    "-DLIBUNWIND_HAS_DL_LIB=OFF",
    # same but -latomic
    "-DLIBCXX_HAS_ATOMIC_LIB=OFF",
    # same but -lc (????)
    "-DLIBCXXABI_HAS_C_LIB=OFF",
]
cmake_dir = "runtimes"
hostmakedepends = [
    "cmake",
    f"llvm{_llvm_majver}-clang-rt-crt-mingw-w64",
    f"llvm{_llvm_majver}-devel",
    "mingw-w64-crt",
    "mingw-w64-headers",
    "mingw-w64-winpthreads",
    "ninja",
    "python",
]
depends = [
    "mingw-w64-crt",
    "mingw-w64-headers",
    "mingw-w64-winpthreads",
]
pkgdesc = "LLVM runtimes for Windows development"
license = "Apache-2.0 WITH LLVM-exception AND NCSA"
url = "https://llvm.org"
source = f"https://github.com/llvm/llvm-project/releases/download/llvmorg-{pkgver}/llvm-project-{pkgver}.src.tar.xz"
sha256 = "d3b86ab29cfb4445a6652e5c2642ccc75e04e38084dde3701d323320f35a31da"
hardening = ["!scp"]
# crosstoolchain
options = ["!check", "empty", "!lto", "!relr"]

_targets = ["x86_64", "i686", "aarch64", "armv7"]


def configure(self):
    from cbuild.util import cmake

    for an in _targets:
        at = an + "-w64-mingw32"
        with self.use_profile(an if an != "i686" else "x86_64"):
            cmake.configure(
                self,
                f"build-{an}",
                self.cmake_dir,
                [
                    *self.configure_args,
                    f"-DCMAKE_SYSROOT=/usr/{at}",
                    # don't let llvm come up with its own triple
                    f"-DLLVM_DEFAULT_TARGET_TRIPLE={at}",
                    f"-DCMAKE_ASM_COMPILER_TARGET={at}",
                    f"-DCMAKE_CXX_COMPILER_TARGET={at}",
                    f"-DCMAKE_C_COMPILER_TARGET={at}",
                ],
                cross_build=False,
            )


def build(self):
    from cbuild.util import cmake

    for an in _targets:
        cmake.build(self, f"build-{an}", ["--verbose"])


def install(self):
    from cbuild.util import cmake

    for an in _targets:
        cmake.install(
            self,
            f"build-{an}",
        )

        at = an + "-w64-mingw32"
        pfx = f"usr/lib/llvm{_llvm_majver}/{at}"

        # libcxx config site
        self.rename(
            f"usr/include/{an}-w64-*",
            f"{pfx}/include",
            relative=False,
            glob=True,
        )

        # target-independent, comes from the host
        self.uninstall("usr/include")
        self.uninstall("usr/share/libc++")
        self.uninstall("usr/lib/*/libc++.modules.json", glob=True)

        # move the libs to the right path
        self.rename(
            f"usr/lib/{an}-w64-*", f"{pfx}/lib", relative=False, glob=True
        )

        # dlls counterparts to .a, move them in together
        self.mv(
            self.destdir / "usr/bin/*.dll",
            self.destdir / f"{pfx}/lib",
            glob=True,
        )

        # make sysroot libs and includes accessible to llvm
        self.install_link(f"{pfx}/mingw", f"../../../{at}")
        self.install_link(f"{pfx}/usr", "mingw")

    self.install_license("LICENSE.TXT")


def _gen(an, at):
    @subpackage(f"llvm{_llvm_majver}-runtimes-mingw-w64-{an}")
    def _(self):
        self.subdesc = an
        self.depends = [
            f"llvm{_llvm_majver}-clang-rt-crt-mingw-w64-{an}",
            f"llvm{_llvm_majver}-runtimes-devel",
            f"mingw-w64-crt-{an}",
            f"mingw-w64-headers-{an}",
            f"mingw-w64-winpthreads-{an}",
        ]
        self.options = ["!strip", "!splitstatic"]
        self.broken_symlinks = [f"usr/lib/llvm{_llvm_majver}/{at}/mingw"]

        return [f"usr/lib/llvm{_llvm_majver}/{at}"]

    depends.append(
        self.with_pkgver(f"llvm{_llvm_majver}-runtimes-mingw-w64-{an}")
    )


for _an in _targets:
    _at = _an + "-w64-mingw32"
    _gen(_an, _at)
