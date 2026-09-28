pkgname = "zlib-ng"
pkgver = "2.2.5"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = ["gtest-devel"]
pkgdesc = "Implementation of zlib compression library with new API"
license = "Zlib"
url = "https://github.com/zlib-ng/zlib-ng"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "5b3b022489f3ced82384f06db1e13ba148cbce38c7941e424d6cb414416acd18"


@subpackage("zlib-ng-devel")
def _(self):
    return self.default_devel()
