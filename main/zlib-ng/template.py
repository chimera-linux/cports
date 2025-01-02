pkgname = "zlib-ng"
pkgver = "2.2.3"
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
sha256 = "f2fb245c35082fe9ea7a22b332730f63cf1d42f04d84fe48294207d033cba4dd"


@subpackage("zlib-ng-devel")
def _(self):
    return self.default_devel()
