pkgname = "quazip"
pkgver = "1.4"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DQUAZIP_ENABLE_TESTS=ON",
    "-DQUAZIP_QT_MAJOR_VERSION=6",
]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "qt6-qt5compat-devel",
    "qt6-qtbase-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "Qt wrapper for minizip"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "LGPL-2.1-or-later WITH custom:static-linking-exception"
url = "https://github.com/stachenov/quazip"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "79633fd3a18e2d11a7d5c40c4c79c1786ba0c74b59ad752e8429746fe1781dd6"


def post_install(self):
    self.install_license("COPYING")


@subpackage("quazip-devel")
def _(self):
    return self.default_devel()
