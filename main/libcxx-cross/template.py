pkgname = "libcxx-cross"
pkgver = "19.1.6"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DCMAKE_BUILD_TYPE=Release",
    "-DCMAKE_C_COMPILER=/usr/bin/clang",
    "-DCMAKE_CXX_COMPILER=/usr/bin/clang++",
    "-DCMAKE_AR=/usr/bin/llvm-ar",
    "-DCMAKE_NM=/usr/bin/llvm-nm",
    "-DCMAKE_RANLIB=/usr/bin/llvm-ranlib",
    "-DLLVM_CONFIG_PATH=/usr/bin/llvm-config",
    "-DCMAKE_C_COMPILER_WORKS=ON",
    "-DCMAKE_CXX_COMPILER_WORKS=ON",
    "-DCMAKE_ASM_COMPILER_WORKS=ON",
    "-DLIBUNWIND_USE_COMPILER_RT=ON",
    "-DLIBUNWIND_ENABLE_ASSERTIONS=OFF",
    "-DLIBCXXABI_ENABLE_STATIC_UNWINDER=OFF",
    "-DLIBCXXABI_USE_LLVM_UNWINDER=ON",
    "-DLIBCXXABI_USE_COMPILER_RT=ON",
    "-DLIBCXX_CXX_ABI=libcxxabi",
    "-DLIBCXX_USE_COMPILER_RT=ON",
    "-DLIBCXX_HAS_MUSL_LIBC=ON",
    "-DLIBCXX_ENABLE_STATIC_ABI_LIBRARY=OFF",
    "-DLIBCXX_HARDENING_MODE=fast",
    "-DLLVM_ENABLE_RUNTIMES=libunwind;libcxxabi;libcxx",
]
hostmakedepends = ["cmake", "ninja", "python"]
makedepends = [
    "clang-rt-crt-cross",
    "libatomic-chimera-cross",
    "musl-cross",
    "linux-headers-cross",
]
depends = [self.with_pkgver("libcxxabi-cross")]
pkgdesc = "Cross-toolchain LLVM libc++"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0 WITH LLVM-exception AND NCSA"
url = "https://llvm.org"
source = f"https://github.com/llvm/llvm-project/releases/download/llvmorg-{pkgver}/llvm-project-{pkgver}.src.tar.xz"
sha256 = "e3f79317adaa9196d2cfffe1c869d7c100b7540832bc44fe0d3f44a12861fa34"
# crosstoolchain
options = ["!cross", "!check", "!lto", "empty"]

cmake_dir = "runtimes"

_targetlist = [
    "aarch64",
    "armhf",
    "armv7",
    "ppc64le",
    "ppc64",
    "ppc",
    "x86_64",
    "riscv64",
]
_targets = sorted(filter(lambda p: p != self.profile().arch, _targetlist))

tool_flags = {
    "CFLAGS": ["-fPIC"],
    "CXXFLAGS": ["-fPIC"],
}


def configure(self):
    from cbuild.util import cmake

    for an in _targets:
        with self.profile(an) as pf:
            at = pf.triplet
            # configure libcxx
            with self.stamp(f"{an}_configure") as s:
                s.check()
                cmake.configure(
                    self,
                    f"build-{an}",
                    self.cmake_dir,
                    [
                        *configure_args,
                        f"-DCMAKE_SYSROOT=/usr/{at}",
                        f"-DCMAKE_ASM_COMPILER_TARGET={at}",
                        f"-DCMAKE_CXX_COMPILER_TARGET={at}",
                        f"-DCMAKE_C_COMPILER_TARGET={at}",
                        f"-DLIBCXX_CXX_ABI_LIBRARY_PATH=/usr/{at}/usr/lib",
                    ],
                    cross_build=False,
                )


def build(self):
    from cbuild.util import cmake

    for an in _targets:
        with self.profile(an):
            with self.stamp(f"{an}_build") as s:
                s.check()
                cmake.build(self, f"build-{an}", ["--verbose"])


def install(self):
    from cbuild.util import cmake

    for an in _targets:
        with self.profile(an) as pf:
            cmake.install(
                self,
                f"build-{an}",
                env={"DESTDIR": str(self.chroot_destdir / "usr" / pf.triplet)},
            )
    self.install_license("LICENSE.TXT")


def _gen_crossp(an, at):
    # libunwind subpackages
    cond = an in _targets

    @subpackage(f"libunwind-cross-{an}-static", cond)
    def _(self):
        self.pkgdesc = "Cross-toolchain LLVM libunwind"
        self.subdesc = f"{an} static library"
        self.depends = [self.with_pkgver(f"libunwind-cross-{an}")]
        return [f"usr/{at}/usr/lib/libunwind.a"]

    @subpackage(f"libunwind-cross-{an}", cond)
    def _(self):
        self.pkgdesc = "Cross-toolchain LLVM libunwind"
        self.subdesc = an
        self.depends = [f"musl-cross-{an}", f"libatomic-chimera-cross-{an}"]
        self.options = [
            "!scanshlibs",
            "!scanrundeps",
            "!splitstatic",
            "foreignelf",
        ]
        return [
            f"usr/{at}/usr/lib/libunwind.*",
            f"usr/{at}/usr/include/*unwind*",
            f"usr/{at}/usr/include/mach-o",
        ]

    # libc++abi subpackages

    @subpackage(f"libcxxabi-cross-{an}-static", cond)
    def _(self):
        self.pkgdesc = "Cross-toolchain LLVM libc++abi"
        self.subdesc = f"{an} static library"
        self.depends = [self.with_pkgver(f"libcxxabi-cross-{an}")]
        return [f"usr/{at}/usr/lib/libc++abi.a"]

    @subpackage(f"libcxxabi-cross-{an}", cond)
    def _(self):
        self.pkgdesc = "Cross-toolchain LLVM libc++abi"
        self.subdesc = an
        self.depends = [self.with_pkgver(f"libunwind-cross-{an}")]
        self.options = [
            "!scanshlibs",
            "!scanrundeps",
            "!splitstatic",
            "foreignelf",
        ]
        return [
            f"usr/{at}/usr/lib/libc++abi*",
            f"usr/{at}/usr/include/c++/v1/*cxxabi*.h",
        ]

    # libc++ subpackages

    @subpackage(f"libcxx-cross-{an}-static", cond)
    def _(self):
        self.subdesc = f"{an} static library"
        self.depends = [
            self.with_pkgver(f"libcxx-cross-{an}"),
        ]
        return [f"usr/{at}/usr/lib/libc++.a"]

    @subpackage(f"libcxx-cross-{an}", cond)
    def _(self):
        self.subdesc = an
        self.depends = [self.with_pkgver(f"libcxxabi-cross-{an}")]
        self.options = [
            "!scanshlibs",
            "!scanrundeps",
            "!splitstatic",
            "foreignelf",
        ]
        return [f"usr/{at}"]

    if cond:
        depends.append(self.with_pkgver(f"libcxx-cross-{an}"))


for _an in _targetlist:
    with self.profile(_an) as _pf:
        _gen_crossp(_an, _pf.triplet)


@subpackage("libunwind-cross-static")
def _(self):
    self.pkgdesc = "Cross-toolchain LLVM libunwind"
    self.depends = []
    self.options = ["empty"]
    for an in _targets:
        self.depends.append(self.with_pkgver(f"libunwind-cross-{an}-static"))

    return []


@subpackage("libcxxabi-cross-static")
def _(self):
    self.pkgdesc = "Cross-toolchain LLVM libc++abi"
    self.depends = []
    self.options = ["empty"]
    for an in _targets:
        self.depends.append(self.with_pkgver(f"libcxxabi-cross-{an}-static"))

    return []


@subpackage("libcxx-cross-static")
def _(self):
    self.subdesc = "static"
    self.depends = []
    self.options = ["empty"]
    for an in _targets:
        self.depends.append(self.with_pkgver(f"libcxx-cross-{an}-static"))

    return []


@subpackage("libunwind-cross")
def _(self):
    self.pkgdesc = "Cross-toolchain LLVM libunwind"
    self.depends = ["musl-cross", "libatomic-chimera-cross"]
    self.options = ["empty"]
    for an in _targets:
        self.depends.append(self.with_pkgver(f"libunwind-cross-{an}"))

    return []


@subpackage("libcxxabi-cross")
def _(self):
    self.pkgdesc = "Cross-toolchain LLVM libcxxabi"
    self.depends = [self.with_pkgver("libunwind-cross")]
    self.options = ["empty"]
    for an in _targets:
        self.depends.append(self.with_pkgver(f"libcxxabi-cross-{an}"))

    return []
