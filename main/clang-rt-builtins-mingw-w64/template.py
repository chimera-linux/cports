pkgname = "clang-rt-builtins-mingw-w64"
pkgver = "19.1.6"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DCMAKE_BUILD_TYPE=Release",
    "-DCMAKE_SYSTEM_NAME=Windows",
    f"-DCMAKE_INSTALL_PREFIX=/usr/lib/clang/{pkgver[0 : pkgver.find('.')]}",
    # prevent executable checks
    "-DCMAKE_TRY_COMPILE_TARGET_TYPE=STATIC_LIBRARY",
    # only build that target
    "-DCOMPILER_RT_DEFAULT_TARGET_ONLY=ON",
    # tools
    "-DCMAKE_C_COMPILER=/usr/bin/clang",
    "-DCMAKE_AR=/usr/bin/llvm-ar",
    "-DCMAKE_NM=/usr/bin/llvm-nm",
    "-DCMAKE_RANLIB=/usr/bin/llvm-ranlib",
    # we are only building builtins at this point
    "-DCOMPILER_RT_BUILD_BUILTINS=ON",
    # disable everything else
    "-DCOMPILER_RT_BUILD_LIBFUZZER=OFF",
    "-DCOMPILER_RT_BUILD_MEMPROF=OFF",
    "-DCOMPILER_RT_BUILD_PROFILE=OFF",
    "-DCOMPILER_RT_BUILD_SANITIZERS=OFF",
    "-DCOMPILER_RT_BUILD_XRAY=OFF",
    "-DCOMPILER_RT_BUILD_ORC=OFF",
]
cmake_dir = "compiler-rt"
hostmakedepends = [
    "base-cross",
    "clang-tools-extra",
    "cmake",
    "llvm-devel",
    "ninja",
    "python",
]
depends = []
pkgdesc = "Clang runtime builtins for Windows development"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "Apache-2.0 WITH LLVM-exception AND NCSA"
url = "https://llvm.org"
source = f"https://github.com/llvm/llvm-project/releases/download/llvmorg-{pkgver}/llvm-project-{pkgver}.src.tar.xz"
sha256 = "e3f79317adaa9196d2cfffe1c869d7c100b7540832bc44fe0d3f44a12861fa34"
hardening = ["!scp"]
# crosstoolchain
options = ["!check", "empty"]

_targets = ["x86_64", "i686", "aarch64", "armv7"]

for _an in _targets:
    hostmakedepends += [
        f"mingw-w64-headers-{_an}",
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
                    f"-DCMAKE_ASM_COMPILER_TARGET={at}",
                    f"-DCMAKE_C_COMPILER_TARGET={at}",
                    f"-DCMAKE_CXX_COMPILER_TARGET={at}",
                ],
                cross_build=False,
            )


def build(self):
    from cbuild.util import cmake

    for an in _targets:
        cmake.build(self, f"build-{an}")


def install(self):
    from cbuild.util import cmake

    for an in _targets:
        cmake.install(self, f"build-{an}")
    self.install_license("LICENSE.TXT")


def _gen(an, at):
    @subpackage(f"clang-rt-builtins-mingw-w64-{an}")
    def _(self):
        match an:
            case "aarch64" | "x86_64":
                suffix = an
            case "armv7":
                suffix = "arm"
            case "i686":
                suffix = "i386"

        self.subdesc = f"{an} support"
        self.depends = ["clang"]
        # strip not supported for COFF
        self.options = ["!strip", "!lintstatic"]

        return [f"usr/lib/clang/*/lib/windows/libclang_rt.builtins-{suffix}.a"]

    depends.append(self.with_pkgver(f"clang-rt-builtins-mingw-w64-{an}"))


for _an in _targets:
    _gen(_an, _an + "-w64-mingw32")
