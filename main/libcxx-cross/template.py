pkgname = "libcxx-cross"
pkgver = "15.0.1"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DCMAKE_BUILD_TYPE=Release", "-Wno-dev",
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
    "-DLIBCXXABI_ENABLE_STATIC_UNWINDER=YES",
    "-DLIBCXXABI_USE_LLVM_UNWINDER=YES",
    "-DLIBCXXABI_USE_COMPILER_RT=YES",
    "-DLIBCXX_CXX_ABI=libcxxabi",
    "-DLIBCXX_USE_COMPILER_RT=YES",
    "-DLIBCXX_HAS_MUSL_LIBC=YES",
    "-DLIBCXX_ENABLE_STATIC_ABI_LIBRARY=YES",
    "-DLLVM_ENABLE_RUNTIMES=libunwind;libcxxabi;libcxx",
]
make_cmd = "make"
hostmakedepends = ["cmake", "python"]
makedepends = ["clang-rt-crt-cross", "musl-cross", "linux-headers-cross"]
depends = [f"libcxxabi-cross={pkgver}-r{pkgrel}"]
pkgdesc = "Cross-toolchain LLVM libc++"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://llvm.org"
source = f"https://github.com/llvm/llvm-project/releases/download/llvmorg-{pkgver}/llvm-project-{pkgver}.src.tar.xz"
sha256 = "f25ce2d4243bebf527284eb7be7f6f56ef454fca8b3de9523f7eb4efb8d26218"
# crosstoolchain
options = ["!cross", "!check", "!lto"]

cmake_dir = "runtimes"

_targets = list(filter(
    lambda p: p != self.profile().arch,
    ["aarch64", "ppc64le", "ppc64", "x86_64", "riscv64"]
))

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
                cmake.configure(self, self.cmake_dir, f"build-{an}", [
                    f"-DCMAKE_SYSROOT=/usr/{at}",
                    f"-DCMAKE_ASM_COMPILER_TARGET={at}",
                    f"-DCMAKE_CXX_COMPILER_TARGET={at}",
                    f"-DCMAKE_C_COMPILER_TARGET={at}",
                    f"-DLIBCXX_CXX_ABI_LIBRARY_PATH=/usr/{at}/usr/lib"
                ], cross_build = False)

def do_build(self):
    for an in _targets:
        with self.profile(an):
            with self.stamp(f"{an}_build") as s:
                s.check()
                self.make.build(wrksrc = f"build-{an}")

def _install_hdrs(self):
    at = self.profile().triplet
    self.install_dir(f"usr/{at}/usr/include/mach-o")
    self.install_file(
        "libunwind/include/__libunwind_config.h",
        f"usr/{at}/usr/include"
    )
    self.install_file(
        "libunwind/include/libunwind.h",
        f"usr/{at}/usr/include"
    )
    self.install_file(
        "libunwind/include/unwind.h",
        f"usr/{at}/usr/include"
    )
    # XXX: 32-bit ARM needs unwind_ehabi.h
    self.install_file(
        "libunwind/include/unwind_itanium.h",
        f"usr/{at}/usr/include"
    )
    self.install_file(
        "libunwind/include/mach-o/compact_unwind_encoding.h",
        f"usr/{at}/usr/include/mach-o"
    )

    self.install_file(
        "libcxxabi/include/__cxxabi_config.h", f"usr/{at}/usr/include"
    )
    self.install_file("libcxxabi/include/cxxabi.h", f"usr/{at}/usr/include")

def do_install(self):
    for an in _targets:
        with self.profile(an) as pf:
            self.make.install(
                ["DESTDIR=" + str(
                    self.chroot_destdir / "usr" / pf.triplet
                )],
                wrksrc = f"build-{an}", default_args = False
            )
            _install_hdrs(self)

def _gen_crossp(an, at):
    # libunwind subpackages

    @subpackage(f"libunwind-cross-{an}-static")
    def _unwst(self):
        self.pkgdesc = f"Cross-toolchain LLVM libunwind ({an} static library)"
        self.depends = [f"libunwind-cross-{an}={pkgver}-r{pkgrel}"]
        return [f"usr/{at}/usr/lib/libunwind.a"]

    @subpackage(f"libunwind-cross-{an}")
    def _unw(self):
        self.pkgdesc = f"Cross-toolchain LLVM libunwind ({an})"
        self.depends = [f"musl-cross-{an}"]
        self.options = [
            "!scanshlibs", "!scanrundeps", "!splitstatic", "foreignelf"
        ]
        return [
            f"usr/{at}/usr/lib/libunwind.*",
            f"usr/{at}/usr/include/*unwind*",
            f"usr/{at}/usr/include/mach-o",
        ]

    # libc++abi subpackages

    @subpackage(f"libcxxabi-cross-{an}-static")
    def _abist(self):
        self.pkgdesc = f"Cross-toolchain LLVM libc++abi ({an} static library)"
        self.depends = [f"libcxxabi-cross-{an}={pkgver}-r{pkgrel}"]
        return [f"usr/{at}/usr/lib/libc++abi.a"]

    @subpackage(f"libcxxabi-cross-{an}")
    def _abi(self):
        self.pkgdesc = f"Cross-toolchain LLVM libc++abi ({an})"
        self.depends = [f"libunwind-cross-{an}={pkgver}-r{pkgrel}"]
        self.options = [
            "!scanshlibs", "!scanrundeps", "!splitstatic", "foreignelf"
        ]
        return [
            f"usr/{at}/usr/lib/libc++abi*",
            f"usr/{at}/usr/include/*cxxabi*.h",
        ]

    # libc++ subpackages

    @subpackage(f"libcxx-cross-{an}-static")
    def _subp(self):
        self.pkgdesc = f"{pkgdesc} ({an} static library)"
        self.depends = [
            f"libcxx-cross-{an}={pkgver}-r{pkgrel}",
        ]
        return [f"usr/{at}/usr/lib/libc++.a"]

    @subpackage(f"libcxx-cross-{an}")
    def _subp(self):
        self.pkgdesc = f"{pkgdesc} ({an})"
        self.depends = [f"libcxxabi-cross-{an}={pkgver}-r{pkgrel}"]
        self.options = [
            "!scanshlibs", "!scanrundeps", "!splitstatic", "foreignelf"
        ]
        return [f"usr/{at}"]

    depends.append(f"libcxx-cross-{an}={pkgver}-r{pkgrel}")

for an in _targets:
    with self.profile(an) as pf:
        _gen_crossp(an, pf.triplet)

@subpackage("libunwind-cross-static")
def _static(self):
    self.pkgdesc = f"Cross-toolchain LLVM libunwind (static)"
    self.depends = []
    self.build_style = "meta"
    for an in _targets:
        self.depends.append(f"libunwind-cross-{an}-static={pkgver}-r{pkgrel}")

    return []

@subpackage("libcxxabi-cross-static")
def _static(self):
    self.pkgdesc = f"Cross-toolchain LLVM libc++abi (static)"
    self.depends = []
    self.build_style = "meta"
    for an in _targets:
        self.depends.append(f"libcxxabi-cross-{an}-static={pkgver}-r{pkgrel}")

    return []

@subpackage("libcxx-cross-static")
def _static(self):
    self.pkgdesc = f"{pkgdesc} (static)"
    self.depends = []
    self.build_style = "meta"
    for an in _targets:
        self.depends.append(f"libcxx-cross-{an}-static={pkgver}-r{pkgrel}")

    return []

@subpackage("libunwind-cross")
def _unw_cross(self):
    self.pkgdesc = "Cross-toolchain LLVM libunwind"
    self.depends = ["musl-cross"]
    self.build_style = "meta"
    for an in _targets:
        self.depends.append(f"libunwind-cross-{an}={pkgver}-r{pkgrel}")

    return []

@subpackage("libcxxabi-cross")
def _cxxabi_cross(self):
    self.pkgdesc = "Cross-toolchain LLVM libcxxabi"
    self.depends = [f"libunwind-cross={pkgver}-r{pkgrel}"]
    self.build_style = "meta"
    for an in _targets:
        self.depends.append(f"libcxxabi-cross-{an}={pkgver}-r{pkgrel}")

    return []
