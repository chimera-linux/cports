pkgname = "ispc"
pkgver = "1.24.0"
pkgrel = 0
archs = ["x86_64", "aarch64", "armv7"]
build_style = "cmake"
configure_args = ["-DCMAKE_BUILD_TYPE=Release"]
hostmakedepends = [
    "bison",
    "cmake",
    "flex",
    "ninja",
    "llvm-tools",
    "python",
]
makedepends = ["clang-devel", "llvm-devel", "ncurses-devel", "onetbb-devel"]
pkgdesc = "Implicit SPMD program compiler"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "BSD-3-Clause"
url = "https://ispc.github.io"
source = f"https://github.com/ispc/ispc/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "617f1339fbfd63216412fcf775cf00d0b350916e88dce7df5c74c1dd422ea42c"


def post_install(self):
    self.install_license("LICENSE.txt")


@subpackage("ispc-libs")
def _libs(self):
    return self.default_libs()


@subpackage("ispc-devel")
def _devel(self):
    return self.default_devel()
