pkgname = "zlib-ng"
pkgver = "2.1.7"
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
sha256 = "59e68f67cbb16999842daeb517cdd86fc25b177b4affd335cd72b76ddc2a46d8"


@subpackage("zlib-ng-devel")
def _devel(self):
    return self.default_devel()
