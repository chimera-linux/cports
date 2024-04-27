pkgname = "clang-rt-crt-mingw-w64"
pkgver = "18.1.5"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DCMAKE_BUILD_TYPE=Release",
    "-DCMAKE_SYSTEM_NAME=Windows",
    "-Wno-dev",
    f"-DCMAKE_INSTALL_PREFIX=/usr/lib/clang/{pkgver[0:pkgver.find('.')]}",
    # prevent executable checks
    "-DCMAKE_TRY_COMPILE_TARGET_TYPE=STATIC_LIBRARY",
    # only build that target
    "-DCOMPILER_RT_DEFAULT_TARGET_ONLY=ON",
    # tools
    "-DCMAKE_C_COMPILER=/usr/bin/clang",
    "-DCMAKE_AR=/usr/bin/llvm-ar",
    "-DCMAKE_NM=/usr/bin/llvm-nm",
    "-DCMAKE_RANLIB=/usr/bin/llvm-ranlib",
    "-DLLVM_CONFIG_PATH=/usr/bin/llvm-config",
    # we are only building builtins and crt at this point
    "-DCOMPILER_RT_BUILD_BUILTINS=ON",
    "-DCOMPILER_RT_BUILD_CRT=ON",
    # disable everything else
    "-DCOMPILER_RT_BUILD_LIBFUZZER=OFF",
    "-DCOMPILER_RT_BUILD_MEMPROF=OFF",
    "-DCOMPILER_RT_BUILD_PROFILE=OFF",
    "-DCOMPILER_RT_BUILD_SANITIZERS=OFF",
    "-DCOMPILER_RT_BUILD_XRAY=OFF",
    "-DCOMPILER_RT_BUILD_ORC=OFF",
    # don't take flags from profile
    "-DCMAKE_C_FLAGS=",
    "-DCMAKE_CXX_FLAGS=",
    "-DCMAKE_LD_FLAGS=",
]
make_cmd = "make"
cmake_dir = "compiler-rt"
hostmakedepends = [
    "clang-tools-extra",
    "cmake",
    "python",
    "llvm-devel",
]
depends = []
pkgdesc = "Compiler runtime for Windows"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "Apache-2.0"
url = "https://llvm.org"
source = f"https://github.com/llvm/llvm-project/releases/download/llvmorg-{pkgver}/llvm-project-{pkgver}.src.tar.xz"
sha256 = "3591a52761a7d390ede51af01ea73abfecc4b1d16445f9d019b67a57edd7de56"
debug_level = 0
hardening = ["!int", "!scp", "!var-init"]
# crosstoolchain
options = ["!cross", "!check", "!lto", "!strip", "empty"]

_targets = ["x86_64", "i686", "aarch64", "armv7"]

for _an in _targets:
    hostmakedepends += [
        f"mingw-w64-headers-{_an}",
    ]
    depends += [f"clang-rt-crt-mingw-w64-{_an}={pkgver}-r{pkgrel}"]


def do_configure(self):
    from cbuild.util import cmake

    for an in _targets:
        at = an + "-w64-mingw32"
        with self.stamp(f"{an}_configure") as s:
            s.check()
            cmake.configure(
                self,
                f"build-{an}",
                self.cmake_dir,
                self.configure_args
                + [
                    f"-DCMAKE_SYSROOT=/usr/{at}",
                    f"-DCMAKE_ASM_COMPILER_TARGET={at}",
                    f"-DCMAKE_C_COMPILER_TARGET={at}",
                    f"-DCMAKE_CXX_COMPILER_TARGET={at}",
                ],
                cross_build=False,
                generator="Unix Makefiles",
            )


def do_build(self):
    from cbuild.util import cmake

    for an in _targets:
        with self.stamp(f"{an}_build") as s:
            s.check()
            cmake.build(self, f"build-{an}")


def do_install(self):
    from cbuild.util import cmake

    for an in _targets:
        cmake.install(self, f"build-{an}")


def _gen(an, at):
    @subpackage(f"clang-rt-crt-mingw-w64-{an}")
    def _subp(self):
        self.pkgdesc = f"{pkgdesc} ({an} support)"
        match an:
            case "aarch64" | "x86_64":
                filename = f"libclang_rt.builtins-{an}.a"
            case "i686":
                filename = "libclang_rt.builtins-i386.a"
            case "armv7":
                filename = "libclang_rt.builtins-arm.a"
        return [f"usr/lib/clang/*/lib/windows/{filename}"]


for _an in _targets:
    _gen(_an, _an + "-w64-mingw32")
