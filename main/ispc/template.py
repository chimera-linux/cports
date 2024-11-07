pkgname = "ispc"
pkgver = "1.25.3"
pkgrel = 0
archs = ["x86_64", "aarch64", "armv7"]
build_style = "cmake"
configure_args = ["-DCMAKE_BUILD_TYPE=Release"]
hostmakedepends = [
    "bison",
    "cmake",
    "flex",
    "llvm-tools",
    "ninja",
    "python",
]
makedepends = [
    "clang-devel",
    "llvm-devel",
    "ncurses-devel",
    "onetbb-devel",
]
pkgdesc = "Implicit SPMD program compiler"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "BSD-3-Clause"
url = "https://ispc.github.io"
source = f"https://github.com/ispc/ispc/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "6f00038e0e86e90474f3117c3b393f6695a8fbe1b3d8fe3b1a0baf197dfb7557"


def post_install(self):
    self.install_license("LICENSE.txt")


@subpackage("ispc-libs")
def _(self):
    return self.default_libs()


@subpackage("ispc-devel")
def _(self):
    return self.default_devel()
