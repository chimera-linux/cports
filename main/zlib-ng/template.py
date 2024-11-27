pkgname = "zlib-ng"
pkgver = "2.2.2"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = ["gtest-devel"]
pkgdesc = "Implementation of zlib compression library with new API"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "Zlib"
url = "https://github.com/zlib-ng/zlib-ng"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "fcb41dd59a3f17002aeb1bb21f04696c9b721404890bb945c5ab39d2cb69654c"


@subpackage("zlib-ng-devel")
def _(self):
    return self.default_devel()
