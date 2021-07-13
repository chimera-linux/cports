pkgname = "libunwind-cross"
version = "12.0.0"
revision = 0
wrksrc = f"llvm-project-{version}.src"
build_style = "cmake"
configure_args = [
    "-DCMAKE_BUILD_TYPE=Release", "-Wno-dev",
    "-DCMAKE_C_COMPILER=/usr/bin/clang",
    "-DCMAKE_CXX_COMPILER=/usr/bin/clang++",
    "-DCMAKE_AR=/usr/bin/llvm-ar",
    "-DCMAKE_NM=/usr/bin/llvm-nm",
    "-DCMAKE_RANLIB=/usr/bin/llvm-ranlib",
    "-DLLVM_CONFIG_PATH=/usr/bin/llvm-config",
]
hostmakedepends = ["cmake"]
makedepends = ["clang-rt-cross-base", "musl-cross"]
depends = ["musl-cross"]
make_cmd = "make"
short_desc = "LLVM libunwind for cross-compiling"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
homepage = "https://llvm.org"
distfiles = [
    f"https://github.com/llvm/llvm-project/releases/download/llvmorg-{version}/llvm-project-{version}.src.tar.xz"
]
checksum = [
    "9ed1688943a4402d7c904cc4515798cdb20080066efa010fe7e1f2551b423628"
]

cmake_dir = "libunwind"

_targets = ["aarch64", "ppc64le", "x86_64"]

# we don't have these available yet; but cmake tests for
# executables with default flags, so avoid trying to use them
CFLAGS = ["--unwindlib=none"]
CXXFLAGS = ["--unwindlib=none", "-nostdlib"]

from cbuild.util import cmake, make
from cbuild import cpu

def init_configure(self):
    self.make = make.Make(self)

def do_configure(self):
    for an in _targets:
        if cpu.target() == an:
            continue

        with self.profile(an):
            at = self.build_profile.triplet
            # configure libunwind
            with self.stamp(f"{an}_configure") as s:
                s.check()
                cmake.configure(self, self.cmake_dir, f"build-{an}", [
                    f"-DCMAKE_SYSROOT=/usr/{at}",
                    f"-DCMAKE_ASM_COMPILER_TARGET={at}",
                    f"-DCMAKE_CXX_COMPILER_TARGET={at}",
                    f"-DCMAKE_C_COMPILER_TARGET={at}"
                ])

def do_build(self):
    for an in _targets:
        if cpu.target() == an:
            continue

        with self.profile(an):
            with self.stamp(f"{an}_build") as s:
                s.check()
                self.make.build(wrksrc = f"build-{an}")

def _install_hdrs(self):
    at = self.build_profile.triplet
    self.install_dir(f"usr/{at}/usr/include/mach-o")
    self.install_file(
        self.abs_wrksrc / "libunwind/include/__libunwind_config.h",
        f"usr/{at}/usr/include"
    )
    self.install_file(
        self.abs_wrksrc / "libunwind/include/libunwind.h",
        f"usr/{at}/usr/include"
    )
    self.install_file(
        self.abs_wrksrc / "libunwind/include/unwind.h",
        f"usr/{at}/usr/include"
    )
    self.install_file(
        self.abs_wrksrc / "libunwind/include/mach-o/compact_unwind_encoding.h",
        f"usr/{at}/usr/include/mach-o"
    )

def do_install(self):
    for an in _targets:
        if cpu.target() == an:
            continue

        with self.profile(an):
            self.make.install(
                ["DESTDIR=" + str(
                    self.chroot_destdir / "usr" / self.build_profile.triplet
                )],
                wrksrc = f"build-{an}", default_args = False
            )
            _install_hdrs(self)

def _gen_crossp(an, at):
    @subpackage(f"libunwind-cross-{an}", cpu.target() != an)
    def _subp(self):
        self.short_desc = f"{short_desc} - {an} support"
        self.depends = [f"musl-cross-{an}"]
        self.noshlibprovides = True
        return [f"usr/{at}"]
    if cpu.target() != an:
        depends.append(f"libunwind-cross-{an}={version}-r{revision}")

for an in _targets:
    with current.profile(an):
        _gen_crossp(an, current.build_profile.triplet)
