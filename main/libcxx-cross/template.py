pkgname = "libcxx-cross"
pkgver = "17.0.6"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DCMAKE_BUILD_TYPE=Release",
    "-Wno-dev",
    "-DCMAKE_C_COMPILER=/usr/bin/clang",
    "-DCMAKE_CXX_COMPILER=/usr/bin/clang++",
    "-DCMAKE_AR=/usr/bin/llvm-ar",
    "-DCMAKE_NM=/usr/bin/llvm-nm",
    "-DCMAKE_RANLIB=/usr/bin/llvm-ranlib",
    "-DLLVM_CONFIG_PATH=/usr/bin/llvm-config",
    "-DCMAKE_C_COMPILER_WORKS=ON",
    "-DCMAKE_CXX_COMPILER_WORKS=ON",
    "-DCMAKE_ASM_COMPILER_WORKS=ON",
    "-DLIBUNWIND_USE_COMPILER_RT=YES",
    "-DLIBCXXABI_ENABLE_STATIC_UNWINDER=NO",
    "-DLIBCXXABI_USE_LLVM_UNWINDER=YES",
    "-DLIBCXXABI_USE_COMPILER_RT=YES",
    "-DLIBCXX_CXX_ABI=libcxxabi",
    "-DLIBCXX_USE_COMPILER_RT=YES",
    "-DLIBCXX_HAS_MUSL_LIBC=YES",
    "-DLIBCXX_ENABLE_STATIC_ABI_LIBRARY=NO",
    "-DLIBCXX_HARDENING_MODE=hardened",
    "-DLLVM_ENABLE_RUNTIMES=libunwind;libcxxabi;libcxx",
]
make_cmd = "make"
hostmakedepends = ["cmake", "python"]
makedepends = [
    "clang-rt-crt-cross",
    "libatomic-chimera-cross",
    "musl-cross",
    "linux-headers-cross",
]
depends = [f"libcxxabi-cross={pkgver}-r{pkgrel}"]
pkgdesc = "Cross-toolchain LLVM libc++"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://llvm.org"
source = f"https://github.com/llvm/llvm-project/releases/download/llvmorg-{pkgver}/llvm-project-{pkgver}.src.tar.xz"
sha256 = "58a8818c60e6627064f312dbf46c02d9949956558340938b71cf731ad8bc0813"
# crosstoolchain
options = ["!cross", "!check", "!lto", "empty"]

cmake_dir = "runtimes"

_targetlist = ["aarch64", "ppc64le", "ppc64", "ppc", "x86_64", "riscv64"]
_targets = sorted(filter(lambda p: p != self.profile().arch, _targetlist))

tool_flags = {
    "CFLAGS": ["-fPIC"],
    "CXXFLAGS": ["-fPIC", "-nostdlib"],
}


def do_configure(self):
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
                    configure_args
                    + [
                        f"-DCMAKE_SYSROOT=/usr/{at}",
                        f"-DCMAKE_ASM_COMPILER_TARGET={at}",
                        f"-DCMAKE_CXX_COMPILER_TARGET={at}",
                        f"-DCMAKE_C_COMPILER_TARGET={at}",
                        f"-DLIBCXX_CXX_ABI_LIBRARY_PATH=/usr/{at}/usr/lib",
                    ],
                    cross_build=False,
                    generator="Unix Makefiles",
                )


def do_build(self):
    from cbuild.util import cmake

    for an in _targets:
        with self.profile(an):
            with self.stamp(f"{an}_build") as s:
                s.check()
                cmake.build(self, f"build-{an}")


def do_install(self):
    from cbuild.util import cmake

    for an in _targets:
        with self.profile(an) as pf:
            cmake.install(
                self,
                f"build-{an}",
                env={"DESTDIR": str(self.chroot_destdir / "usr" / pf.triplet)},
            )


def _gen_crossp(an, at):
    # libunwind subpackages
    cond = an in _targets

    @subpackage(f"libunwind-cross-{an}-static", cond)
    def _unwst(self):
        self.pkgdesc = f"Cross-toolchain LLVM libunwind ({an} static library)"
        self.depends = [f"libunwind-cross-{an}={pkgver}-r{pkgrel}"]
        return [f"usr/{at}/usr/lib/libunwind.a"]

    @subpackage(f"libunwind-cross-{an}", cond)
    def _unw(self):
        self.pkgdesc = f"Cross-toolchain LLVM libunwind ({an})"
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
    def _abist(self):
        self.pkgdesc = f"Cross-toolchain LLVM libc++abi ({an} static library)"
        self.depends = [f"libcxxabi-cross-{an}={pkgver}-r{pkgrel}"]
        return [f"usr/{at}/usr/lib/libc++abi.a"]

    @subpackage(f"libcxxabi-cross-{an}", cond)
    def _abi(self):
        self.pkgdesc = f"Cross-toolchain LLVM libc++abi ({an})"
        self.depends = [f"libunwind-cross-{an}={pkgver}-r{pkgrel}"]
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
    def _subp_static(self):
        self.pkgdesc = f"{pkgdesc} ({an} static library)"
        self.depends = [
            f"libcxx-cross-{an}={pkgver}-r{pkgrel}",
        ]
        return [f"usr/{at}/usr/lib/libc++.a"]

    @subpackage(f"libcxx-cross-{an}", cond)
    def _subp(self):
        self.pkgdesc = f"{pkgdesc} ({an})"
        self.depends = [f"libcxxabi-cross-{an}={pkgver}-r{pkgrel}"]
        self.options = [
            "!scanshlibs",
            "!scanrundeps",
            "!splitstatic",
            "foreignelf",
        ]
        return [f"usr/{at}"]

    if cond:
        depends.append(f"libcxx-cross-{an}={pkgver}-r{pkgrel}")


for _an in _targetlist:
    with self.profile(_an) as _pf:
        _gen_crossp(_an, _pf.triplet)


@subpackage("libunwind-cross-static")
def _unw_static(self):
    self.pkgdesc = "Cross-toolchain LLVM libunwind (static)"
    self.depends = []
    self.options = ["empty"]
    for an in _targets:
        self.depends.append(f"libunwind-cross-{an}-static={pkgver}-r{pkgrel}")

    return []


@subpackage("libcxxabi-cross-static")
def _abi_static(self):
    self.pkgdesc = "Cross-toolchain LLVM libc++abi (static)"
    self.depends = []
    self.options = ["empty"]
    for an in _targets:
        self.depends.append(f"libcxxabi-cross-{an}-static={pkgver}-r{pkgrel}")

    return []


@subpackage("libcxx-cross-static")
def _cxx_static(self):
    self.pkgdesc = f"{pkgdesc} (static)"
    self.depends = []
    self.options = ["empty"]
    for an in _targets:
        self.depends.append(f"libcxx-cross-{an}-static={pkgver}-r{pkgrel}")

    return []


@subpackage("libunwind-cross")
def _unw_cross(self):
    self.pkgdesc = "Cross-toolchain LLVM libunwind"
    self.depends = ["musl-cross", "libatomic-chimera-cross"]
    self.options = ["empty"]
    for an in _targets:
        self.depends.append(f"libunwind-cross-{an}={pkgver}-r{pkgrel}")

    return []


@subpackage("libcxxabi-cross")
def _cxxabi_cross(self):
    self.pkgdesc = "Cross-toolchain LLVM libcxxabi"
    self.depends = [f"libunwind-cross={pkgver}-r{pkgrel}"]
    self.options = ["empty"]
    for an in _targets:
        self.depends.append(f"libcxxabi-cross-{an}={pkgver}-r{pkgrel}")

    return []
