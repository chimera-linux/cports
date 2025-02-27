pkgname = "zlib-ng"
pkgver = "2.2.4"
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
sha256 = "a73343c3093e5cdc50d9377997c3815b878fd110bf6511c2c7759f2afb90f5a3"


@subpackage("zlib-ng-devel")
def _(self):
    return self.default_devel()
