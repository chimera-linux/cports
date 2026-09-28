pkgname = "kdsingleapplication"
pkgver = "1.2.1"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DKDSingleApplication_EXAMPLES=OFF",
    "-DKDSingleApplication_TESTS=ON",
]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = ["qt6-qtbase-devel"]
pkgdesc = "Helper class for single-instance applications"
license = "MIT"
url = "https://github.com/KDAB/KDSingleApplication"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "e3254ce9dc5ecf6d61ef83264bc61d486a307f0e3c9ed1bb2176f068cdbcbe09"


def post_install(self):
    self.install_license("LICENSE.txt")


@subpackage("kdsingleapplication-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]
    return self.default_devel()
