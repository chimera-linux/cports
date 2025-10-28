pkgname = "llvm-runtimes-cross"
pkgver = "21.1.4"
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
hostmakedepends = ["clang-tools-extra", "cmake", "ninja", "python"]
makedepends = [
    "clang-devel",
    "clang-rt-crt-cross",
    "libatomic-chimera-cross",
    "linux-headers-cross",
    "llvm-devel",
    "musl-cross",
]
depends = [self.with_pkgver("llvm-runtimes-cross-libcxx")]
pkgdesc = "Cross-toolchain LLVM runtimes"
license = "Apache-2.0 WITH LLVM-exception AND NCSA"
url = "https://llvm.org"
source = f"https://github.com/llvm/llvm-project/releases/download/llvmorg-{pkgver}/llvm-project-{pkgver}.src.tar.xz"
sha256 = "a01ad7e5167780c945871d75c0413081d12067607a6de5cf71dc3e8d1a82112c"
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
    "loongarch64",
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

    @subpackage(f"llvm-runtimes-cross-libunwind-{an}-static", cond)
    def _(self):
        self.subdesc = f"{an} static libunwind"
        self.depends = [self.with_pkgver(f"llvm-runtimes-cross-libunwind-{an}")]
        # transitional
        self.provides = [self.with_pkgver(f"libunwind-cross-{an}-static")]
        return [f"usr/{at}/usr/lib/libunwind.a"]

    @subpackage(f"llvm-runtimes-cross-libunwind-{an}", cond)
    def _(self):
        self.subdesc = f"{an} libunwind"
        self.depends = [f"musl-cross-{an}", f"libatomic-chimera-cross-{an}"]
        self.options = [
            "!scanshlibs",
            "!scanrundeps",
            "!splitstatic",
            "foreignelf",
        ]
        # transitional
        self.provides = [self.with_pkgver(f"libunwind-cross-{an}")]
        return [
            f"usr/{at}/usr/lib/libunwind.*",
            f"usr/{at}/usr/include/*unwind*",
            f"usr/{at}/usr/include/mach-o",
        ]

    # libc++abi subpackages

    @subpackage(f"llvm-runtimes-cross-libcxxabi-{an}-static", cond)
    def _(self):
        self.subdesc = f"{an} static libcxxabi"
        self.depends = [self.with_pkgver(f"llvm-runtimes-cross-libcxxabi-{an}")]
        # transitional
        self.provides = [self.with_pkgver(f"libcxxabi-cross-{an}-static")]
        return [f"usr/{at}/usr/lib/libc++abi.a"]

    @subpackage(f"llvm-runtimes-cross-libcxxabi-{an}", cond)
    def _(self):
        self.subdesc = f"{an} libcxxabi"
        self.depends = [self.with_pkgver(f"llvm-runtimes-cross-libunwind-{an}")]
        self.options = [
            "!scanshlibs",
            "!scanrundeps",
            "!splitstatic",
            "foreignelf",
        ]
        # transitional
        self.provides = [self.with_pkgver(f"libcxxabi-cross-{an}")]
        return [
            f"usr/{at}/usr/lib/libc++abi*",
            f"usr/{at}/usr/include/c++/v1/*cxxabi*.h",
        ]

    # libc++ subpackages

    @subpackage(f"llvm-runtimes-cross-libcxx-{an}-static", cond)
    def _(self):
        self.subdesc = f"{an} static libcxx"
        self.depends = [self.with_pkgver(f"llvm-runtimes-cross-libcxx-{an}")]
        # transitional
        self.provides = [self.with_pkgver(f"libcxx-cross-{an}-static")]
        return [f"usr/{at}/usr/lib/libc++.a"]

    @subpackage(f"llvm-runtimes-cross-libcxx-{an}", cond)
    def _(self):
        self.subdesc = f"{an} libcxx"
        self.depends = [self.with_pkgver(f"llvm-runtimes-cross-libcxxabi-{an}")]
        self.options = [
            "!scanshlibs",
            "!scanrundeps",
            "!splitstatic",
            "foreignelf",
        ]
        # transitional
        self.provides = [self.with_pkgver(f"libcxx-cross-{an}")]
        return [f"usr/{at}"]

    # general subpackages

    @subpackage(f"llvm-runtimes-cross-{an}-static", cond)
    def _(self):
        self.subdesc = f"{an} static"
        self.depends = [
            self.with_pkgver(f"llvm-runtimes-cross-libunwind-{an}-static"),
            self.with_pkgver(f"llvm-runtimes-cross-libcxxabi-{an}-static"),
            self.with_pkgver(f"llvm-runtimes-cross-libcxx-{an}-static"),
        ]
        self.options = ["empty"]
        return []

    @subpackage(f"llvm-runtimes-cross-{an}", cond)
    def _(self):
        self.subdesc = an
        self.depends = [self.with_pkgver(f"llvm-runtimes-cross-libcxx-{an}")]
        self.options = ["empty"]
        return []


for _an in _targetlist:
    with self.profile(_an) as _pf:
        _gen_crossp(_an, _pf.triplet)


@subpackage("llvm-runtimes-cross-libunwind-static")
def _(self):
    self.subdesc = "static libunwind"
    self.depends = []
    self.options = ["empty"]
    # transitional
    self.provides = [self.with_pkgver("libunwind-cross-static")]
    for an in _targets:
        self.depends.append(
            self.with_pkgver(f"llvm-runtimes-cross-libunwind-{an}-static")
        )

    return []


@subpackage("llvm-runtimes-cross-libcxxabi-static")
def _(self):
    self.subdesc = "static libcxxabi"
    self.depends = []
    self.options = ["empty"]
    # transitional
    self.provides = [self.with_pkgver("libcxxabi-cross-static")]
    for an in _targets:
        self.depends.append(
            self.with_pkgver(f"llvm-runtimes-cross-libcxxabi-{an}-static")
        )

    return []


@subpackage("llvm-runtimes-cross-libcxx-static")
def _(self):
    self.subdesc = "static libcxx"
    self.depends = []
    self.options = ["empty"]
    # transitional
    self.provides = [self.with_pkgver("libcxx-cross-static")]
    for an in _targets:
        self.depends.append(
            self.with_pkgver(f"llvm-runtimes-cross-libcxx-{an}-static")
        )

    return []


@subpackage("llvm-runtimes-cross-static")
def _(self):
    self.subdesc = "static"
    self.depends = [
        self.with_pkgver("llvm-runtimes-cross-libunwind-static"),
        self.with_pkgver("llvm-runtimes-cross-libcxxabi-static"),
        self.with_pkgver("llvm-runtimes-cross-libcxx-static"),
    ]
    self.options = ["empty"]

    return []


@subpackage("llvm-runtimes-cross-libunwind")
def _(self):
    self.subdesc = "libunwind"
    self.depends = ["musl-cross", "libatomic-chimera-cross"]
    self.options = ["empty"]
    # transitional
    self.provides = [self.with_pkgver("libunwind-cross")]
    for an in _targets:
        self.depends.append(
            self.with_pkgver(f"llvm-runtimes-cross-libunwind-{an}")
        )

    return []


@subpackage("llvm-runtimes-cross-libcxxabi")
def _(self):
    self.subdesc = "libcxxabi"
    self.depends = [self.with_pkgver("llvm-runtimes-cross-libunwind")]
    self.options = ["empty"]
    # transitional
    self.provides = [self.with_pkgver("libcxxabi-cross")]
    for an in _targets:
        self.depends.append(
            self.with_pkgver(f"llvm-runtimes-cross-libcxxabi-{an}")
        )

    return []


@subpackage("llvm-runtimes-cross-libcxx")
def _(self):
    self.subdesc = "libcxx"
    self.depends = [self.with_pkgver("llvm-runtimes-cross-libcxxabi")]
    self.options = ["empty"]
    # transitional
    self.provides = [self.with_pkgver("libcxx-cross")]
    for an in _targets:
        self.depends.append(
            self.with_pkgver(f"llvm-runtimes-cross-libcxx-{an}")
        )

    return []
