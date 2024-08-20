pkgname = "zlib-ng"
pkgver = "2.2.1"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = ["gtest-devel"]
pkgdesc = "Implementation of zlib compression library with new API"
maintainer = "psykose <alice@ayaya.dev>"
license = "Zlib"
url = "https://github.com/zlib-ng/zlib-ng"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "ec6a76169d4214e2e8b737e0850ba4acb806c69eeace6240ed4481b9f5c57cdf"


@subpackage("zlib-ng-devel")
def _(self):
    return self.default_devel()
