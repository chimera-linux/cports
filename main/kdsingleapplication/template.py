pkgname = "kdsingleapplication"
pkgver = "1.2.0"
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
sha256 = "ff4ae6a4620beed1cdb3e6a9b78a17d7d1dae7139c3d4746d4856b7547d42c38"


def post_install(self):
    self.install_license("LICENSE.txt")


@subpackage("kdsingleapplication-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]
    return self.default_devel()
