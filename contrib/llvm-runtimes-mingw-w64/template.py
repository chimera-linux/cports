pkgname = "llvm-runtimes-mingw-w64"
pkgver = "18.1.5"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DCMAKE_SYSTEM_NAME=Windows",
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
    "-DLIBUNWIND_ENABLE_SHARED=NO",
    "-DLIBCXX_USE_COMPILER_RT=YES",
    "-DLIBCXX_ENABLE_STATIC_ABI_LIBRARY=ON",
    "-DLIBCXX_ENABLE_SHARED=OFF",
    "-DLIBCXX_CXX_ABI=libcxxabi",
    "-DLIBCXXABI_USE_COMPILER_RT=ON",
    "-DLIBCXXABI_USE_LLVM_UNWINDER=ON",
    "-DLIBCXXABI_ENABLE_SHARED=OFF",
    "-DLLVM_ENABLE_RUNTIMES=libcxx;libcxxabi;libunwind",
]
make_cmd = "make"
hostmakedepends = ["cmake", "python"]
depends = []
pkgdesc = "LLVM runtimes for Windows"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "Apache-2.0"
url = "https://llvm.org"
source = f"https://github.com/llvm/llvm-project/releases/download/llvmorg-{pkgver}/llvm-project-{pkgver}.src.tar.xz"
sha256 = "3591a52761a7d390ede51af01ea73abfecc4b1d16445f9d019b67a57edd7de56"
# crosstoolchain
options = ["!cross", "!check", "!lto", "empty"]

cmake_dir = "runtimes"

_targets = ["x86_64", "i686", "aarch64", "armv7"]

for _an in _targets:
    hostmakedepends += [f"mingw-w64-headers-{_an}", f"mingw-w64-crt-{_an}"]
    depends += [f"libunwind-mingw-w64-{_an}={pkgver}-r{pkgrel}"]


def do_configure(self):
    from cbuild.util import cmake

    for an in _targets:
        at = an + "-w64-mingw32"
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
                    f"-DCMAKE_INSTALL_PREFIX=/usr/{at}",
                    f"-DCMAKE_ASM_COMPILER_TARGET={at}",
                    f"-DCMAKE_CXX_COMPILER_TARGET={at}",
                    f"-DCMAKE_C_COMPILER_TARGET={at}",
                    f"-DLIBCXX_CXX_ABI_LIBRARY_PATH=/usr/{at}/lib",
                ],
                cross_build=False,
                generator="Unix Makefiles",
                env={
                    "CFLAGS": "",
                    "CXXFLAGS": "",
                    "LDFLAGS": "",
                },
            )


def do_build(self):
    from cbuild.util import cmake

    for an in _targets:
        with self.stamp(f"{an}_build") as s:
            s.check()
            cmake.build(self, f"build-{an}", ["--verbose"])


def do_install(self):
    from cbuild.util import cmake

    for an in _targets:
        cmake.install(
            self,
            f"build-{an}",
        )


def _gen(an, at):
    @subpackage(f"llvm-runtimes-mingw-w64-{an}")
    def _subp(self):
        self.pkgdesc = f"{pkgdesc} ({an} support)"
        return [f"usr/{at}"]


for _an in _targets:
    _at = _an + "-w64-mingw32"
    _gen(_an, _at)
