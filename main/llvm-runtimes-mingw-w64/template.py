pkgname = "llvm-runtimes-mingw-w64"
pkgver = "19.1.7"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DCMAKE_SYSTEM_NAME=Windows",
    "-DCMAKE_BUILD_TYPE=Release",
    "-DCMAKE_C_COMPILER=/usr/bin/clang",
    "-DCMAKE_CXX_COMPILER=/usr/bin/clang++",
    "-DCMAKE_AR=/usr/bin/llvm-ar",
    "-DCMAKE_NM=/usr/bin/llvm-nm",
    "-DCMAKE_RANLIB=/usr/bin/llvm-ranlib",
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
    "base-cross",
    "clang-devel-static",
    "clang-tools-extra",
    "cmake",
    "llvm-devel",
    "ninja",
    "python",
]
depends = [
    self.with_pkgver("llvm-runtimes-mingw-w64-libcxx"),
    "mingw-w64-headers",
]
pkgdesc = "LLVM libc++ for Windows development"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "Apache-2.0 WITH LLVM-exception AND NCSA"
url = "https://llvm.org"
source = f"https://github.com/llvm/llvm-project/releases/download/llvmorg-{pkgver}/llvm-project-{pkgver}.src.tar.xz"
sha256 = "82401fea7b79d0078043f7598b835284d6650a75b93e64b6f761ea7b63097501"
hardening = ["!scp"]
# crosstoolchain
options = ["!check", "empty", "!relr"]

_targets = ["x86_64", "i686", "aarch64", "armv7"]


for _an in _targets:
    hostmakedepends += [
        f"mingw-w64-crt-{_an}",
        f"mingw-w64-winpthreads-{_an}",
        f"clang-rt-builtins-mingw-w64-{_an}",
    ]


def configure(self):
    from cbuild.util import cmake

    for an in _targets:
        at = an + "-w64-mingw32"
        with self.profile(an if an != "i686" else "x86_64"):
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

    self.install_license("LICENSE.TXT")

    for an in _targets:
        cmake.install(
            self,
            f"build-{an}",
        )

        # move target-specific paths to sysroot so clang can find them later
        at = an + "-w64-mingw32"
        self.rename(
            f"usr/include/{an}-w64-*",
            f"usr/{at}/include",
            relative=False,
            glob=True,
        )
        self.rename(
            f"usr/lib/{an}-w64-*", f"usr/{at}/lib", relative=False, glob=True
        )
        self.rename("usr/share/libc++", f"usr/{at}/share", relative=False)

        # why are dlls installed to a target-agnostic path anyway????
        self.rename("usr/bin", f"usr/{at}/bin", relative=False)

    # yoink remaining (target-agnostic) files
    self.uninstall("usr/include")
    self.uninstall("usr/lib")


def _gen(an, at):
    @subpackage(f"llvm-runtimes-mingw-w64-libunwind-{an}")
    def _(self):
        self.pkgdesc = "LLVM libunwind for Windows development"
        self.subdesc = an
        self.depends = [f"mingw-w64-crt-{an}"]
        # strip not supported for COFF
        self.options = ["!strip"]
        # transitional
        self.provides = [self.with_pkgver(f"libunwind-mingw-w64-{an}")]

        return [
            f"usr/{at}/lib/libunwind.*",
        ]

    @subpackage(f"llvm-runtimes-mingw-w64-libcxxabi-{an}")
    def _(self):
        self.pkgdesc = "LLVM libc++abi for Windows development"
        self.subdesc = an
        self.depends = [
            self.with_pkgver(f"llvm-runtimes-mingw-w64-libunwind-{an}")
        ]
        self.options = ["!strip"]
        # transitional
        self.provides = [self.with_pkgver(f"libcxxabi-mingw-w64-{an}")]

        return [
            f"usr/{at}/lib/libc++abi*",
        ]

    @subpackage(f"llvm-runtimes-mingw-w64-libcxx-{an}")
    def _(self):
        self.subdesc = an
        self.depends = [
            self.with_pkgver(f"llvm-runtimes-mingw-w64-libcxxabi-{an}"),
            # host headers
            "libcxx-devel",
            # for include_next
            f"mingw-w64-headers-{an}",
        ]
        self.options = ["!strip"]
        # transitional
        self.provides = [self.with_pkgver(f"libcxx-mingw-w64-{an}")]

        return [f"usr/{at}"]

    @subpackage(f"llvm-runtimes-mingw-w64-{an}")
    def _(self):
        self.subdesc = an
        self.depends = [
            self.with_pkgver(f"llvm-runtimes-mingw-w64-libcxx-{an}")
        ]
        self.options = ["empty"]
        return []


for _an in _targets:
    _at = _an + "-w64-mingw32"
    _gen(_an, _at)


@subpackage("llvm-runtimes-mingw-w64-libunwind")
def _(self):
    self.pkgdesc = "LLVM libunwind for Windows development"
    self.depends = ["mingw-w64-crt"]
    self.options = ["empty"]
    # transitional
    self.provides = [self.with_pkgver("libunwind-mingw-w64")]
    for an in _targets:
        self.depends.append(self.with_pkgver(f"libunwind-mingw-w64-{an}"))

    return []


@subpackage("llvm-runtimes-mingw-w64-libcxxabi")
def _(self):
    self.pkgdesc = "LLVM libc++abi for Windows development"
    self.depends = [self.with_pkgver("llvm-runtimes-mingw-w64-libunwind")]
    self.options = ["empty"]
    # transitional
    self.provides = [self.with_pkgver("libcxxabi-mingw-w64")]
    for an in _targets:
        self.depends.append(self.with_pkgver(f"libcxxabi-mingw-w64-{an}"))

    return []


@subpackage("llvm-runtimes-mingw-w64-libcxx")
def _(self):
    self.pkgdesc = "LLVM libc++ for Windows development"
    self.depends = [self.with_pkgver("llvm-runtimes-mingw-w64-libcxxabi")]
    self.options = ["empty"]
    # transitional
    self.provides = [self.with_pkgver("libcxx-mingw-w64")]
    for an in _targets:
        self.depends.append(self.with_pkgver(f"libcxx-mingw-w64-{an}"))

    return []
