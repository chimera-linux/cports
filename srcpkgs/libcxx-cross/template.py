pkgname = "libcxx-cross"
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
    "-DLIBCXX_CXX_ABI=libcxxabi",
    "-DLIBCXX_USE_COMPILER_RT=YES",
    "-DLIBCXX_HAS_MUSL_LIBC=YES",
    "-DLIBCXXABI_USE_LLVM_UNWINDER=YES",
    "-DLIBCXX_ENABLE_STATIC_ABI_LIBRARY=YES",
]
hostmakedepends = ["cmake", "python"]
makedepends = ["libcxxabi-cross", "kernel-libc-headers-cross"]
depends = ["libcxxabi-cross"]
make_cmd = "make"
short_desc = "LLVM libc++ for cross-compiling"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
homepage = "https://llvm.org"
distfiles = [
    f"https://github.com/llvm/llvm-project/releases/download/llvmorg-{version}/llvm-project-{version}.src.tar.xz"
]
checksum = [
    "9ed1688943a4402d7c904cc4515798cdb20080066efa010fe7e1f2551b423628"
]
nocross = True

cmake_dir = "libcxx"

_targets = list(filter(
    lambda p: p != current.build_profile.arch,
    ["aarch64", "ppc64le", "ppc64", "x86_64", "riscv64"]
))

# not available yet, prevent cmake checks
CFLAGS = ["-fPIC"]
CXXFLAGS = ["-fPIC", "-nostdlib"]

from cbuild.util import cmake, make

def init_configure(self):
    self.make = make.Make(self)

def do_configure(self):
    for an in _targets:
        with self.profile(an):
            at = self.build_profile.short_triplet
            # configure libcxx
            with self.stamp(f"{an}_configure") as s:
                s.check()
                cmake.configure(self, self.cmake_dir, f"build-{an}", [
                    f"-DCMAKE_SYSROOT=/usr/{at}",
                    f"-DCMAKE_ASM_COMPILER_TARGET={at}",
                    f"-DCMAKE_CXX_COMPILER_TARGET={at}",
                    f"-DCMAKE_C_COMPILER_TARGET={at}",
                    f"-DLIBCXX_CXX_ABI_LIBRARY_PATH=/usr/{at}/usr/lib"
                ])

def do_build(self):
    for an in _targets:
        with self.profile(an):
            with self.stamp(f"{an}_build") as s:
                s.check()
                self.make.build(wrksrc = f"build-{an}")

def do_install(self):
    for an in _targets:
        with self.profile(an):
            self.make.install(
                ["DESTDIR=" + str(
                    self.chroot_destdir / "usr" / self.build_profile.short_triplet
                )],
                wrksrc = f"build-{an}", default_args = False
            )

def _gen_crossp(an, at):
    @subpackage(f"libcxx-cross-{an}")
    def _subp(self):
        self.short_desc = f"{short_desc} - {an} support"
        self.depends = [f"libcxxabi-cross-{an}"]
        self.options = ["!scanshlibs"]
        return [f"usr/{at}"]
    depends.append(f"libcxx-cross-{an}={version}-r{revision}")

for an in _targets:
    with current.profile(an):
        _gen_crossp(an, current.build_profile.short_triplet)
