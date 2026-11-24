pkgname = "llvm23-clang-rt-crt-mingw-w64"
pkgver = "23.1.6"
_llvm_majver = pkgver[0:2]
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DCMAKE_BUILD_TYPE=Release",
    "-DCMAKE_SYSTEM_NAME=Windows",
    f"-DCMAKE_INSTALL_PREFIX=/usr/lib/llvm{_llvm_majver}/lib/clang/{_llvm_majver}",
    # prevent executable checks
    "-DCMAKE_TRY_COMPILE_TARGET_TYPE=STATIC_LIBRARY",
    # only build that target
    "-DCOMPILER_RT_DEFAULT_TARGET_ONLY=ON",
    # tools
    f"-DCMAKE_C_COMPILER=/usr/bin/clang-{_llvm_majver}",
    f"-DCMAKE_CXX_COMPILER=/usr/bin/clang++-{_llvm_majver}",
    f"-DCMAKE_AR=/usr/bin/llvm-ar-{_llvm_majver}",
    f"-DCMAKE_NM=/usr/bin/llvm-nm-{_llvm_majver}",
    f"-DCMAKE_RANLIB=/usr/bin/llvm-ranlib-{_llvm_majver}",
    f"-DLLVM_CONFIG_PATH=/usr/bin/llvm-config-{_llvm_majver}",
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
    "cmake",
    f"llvm{_llvm_majver}-devel",
    "mingw-w64-headers",
    "ninja",
    "python",
]
depends = []
pkgdesc = "Clang runtime builtins for Windows development"
license = "Apache-2.0 WITH LLVM-exception AND NCSA"
url = "https://llvm.org"
source = f"https://github.com/llvm/llvm-project/releases/download/llvmorg-{pkgver}/llvm-project-{pkgver}.src.tar.xz"
sha256 = "d3b86ab29cfb4445a6652e5c2642ccc75e04e38084dde3701d323320f35a31da"
hardening = ["!scp"]
# crosstoolchain
options = ["!check", "empty"]

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


def _gen(an):
    @subpackage(f"llvm{_llvm_majver}-clang-rt-crt-mingw-w64-{an}")
    def _(self):
        match an:
            case "aarch64" | "x86_64":
                suffix = an
            case "armv7":
                suffix = "arm"
            case "i686":
                suffix = "i386"

        self.subdesc = f"{an} support"
        self.depends = [f"llvm{_llvm_majver}-clang"]
        # strip not supported for COFF
        self.options = ["!strip", "!lintstatic"]

        return [
            f"usr/lib/llvm{_llvm_majver}/lib/clang/{_llvm_majver}/lib/windows/libclang_rt.builtins-{suffix}.a"
        ]

    depends.append(
        self.with_pkgver(f"llvm{_llvm_majver}-clang-rt-crt-mingw-w64-{an}")
    )


for _an in _targets:
    _gen(_an)
