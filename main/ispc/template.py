pkgname = "ispc"
pkgver = "1.25.2"
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
sha256 = "745cc8bcde26e63af2700f1811b66d2ca66b2844c8e2aa9ac19c12ab6a39b82a"


def post_install(self):
    self.install_license("LICENSE.txt")


@subpackage("ispc-libs")
def _(self):
    return self.default_libs()


@subpackage("ispc-devel")
def _(self):
    return self.default_devel()
