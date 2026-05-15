pkgname = "llvm-runtimes-cross"
pkgver = "22.1.4"
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
    "clang-devel",
    "clang-rt-crt-cross",
    "libatomic-chimera-cross",
    "linux-headers-cross",
    "llvm-devel",
    "musl-cross",
]
depends = ["musl-cross", "libatomic-chimera-cross"]
renames = [
    "llvm-runtimes-cross-libcxx",
    "llvm-runtimes-cross-libcxxabi",
    "llvm-runtimes-cross-libunwind",
    "libcxx-cross",
    "libcxxabi-cross",
    "libunwind-cross",
]
pkgdesc = "Cross-toolchain LLVM runtimes"
license = "Apache-2.0 WITH LLVM-exception AND NCSA"
url = "https://llvm.org"
source = f"https://github.com/llvm/llvm-project/releases/download/llvmorg-{pkgver}/llvm-project-{pkgver}.src.tar.xz"
sha256 = "3e68c90dda630c27d41d201e37b8bbf5222e39b273dec5ca880709c69e0a07d4"
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

for _an in _targets:
    depends += [f"llvm-runtimes-cross-{_an}"]

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


@subpackage("llvm-runtimes-cross-static")
def _(self):
    self.subdesc = "static"
    self.renames = [
        "llvm-runtimes-cross-libcxx-static",
        "llvm-runtimes-cross-libcxxabi-static",
        "llvm-runtimes-cross-libunwind-static",
        "libcxx-cross-static",
        "libcxxabi-cross-static",
        "libunwind-cross-static",
    ]
    self.depends = [self.parent]
    for an in _targets:
        self.depends.append(
            self.with_pkgver(f"llvm-runtimes-cross-{an}-static")
        )
    self.options = ["empty"]

    return []


def _gen_crossp(an, at):
    cond = an in _targets

    @subpackage(f"llvm-runtimes-cross-{an}-static", cond)
    def _(self):
        self.subdesc = f"{an} static libraries"
        self.renames = [
            f"llvm-runtimes-cross-libcxx-{an}-static",
            f"llvm-runtimes-cross-libcxxabi-{an}-static",
            f"llvm-runtimes-cross-libunwind-{an}-static",
            f"libcxx-cross-{an}-static",
            f"libcxxabi-cross-{an}-static",
            f"libunwind-cross-{an}-static",
        ]
        self.depends = [self.with_pkgver(f"llvm-runtimes-cross-{an}")]
        return [f"usr/{at}/usr/lib/*.a"]

    @subpackage(f"llvm-runtimes-cross-{an}", cond)
    def _(self):
        self.subdesc = an
        self.renames = [
            f"llvm-runtimes-cross-libcxx-{an}",
            f"llvm-runtimes-cross-libcxxabi-{an}",
            f"llvm-runtimes-cross-libunwind-{an}",
            f"libcxx-cross-{an}",
            f"libcxxabi-cross-{an}",
            f"libunwind-cross-{an}",
        ]
        self.depends = [f"musl-cross-{an}", f"libatomic-chimera-cross-{an}"]
        self.options = [
            "!scanshlibs",
            "!scanrundeps",
            "!splitstatic",
            "foreignelf",
        ]
        return [f"usr/{at}"]


for _an in _targetlist:
    with self.profile(_an) as _pf:
        _gen_crossp(_an, _pf.triplet)
