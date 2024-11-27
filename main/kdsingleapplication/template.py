pkgname = "kdsingleapplication"
pkgver = "1.1.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DKDSingleApplication_QT6=ON",
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
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "MIT"
url = "https://github.com/KDAB/KDSingleApplication"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "1f19124c0aa5c6fffee3da174f7d2e091fab6dca1e123da70bb0fe615bfbe3e8"


def post_install(self):
    self.install_license("LICENSE.txt")


@subpackage("kdsingleapplication-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]
    return self.default_devel()
