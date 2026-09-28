pkgname = "quazip"
pkgver = "1.5"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DQUAZIP_ENABLE_TESTS=ON",
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
license = "LGPL-2.1-or-later WITH custom:static-linking-exception"
url = "https://github.com/stachenov/quazip"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "405b72b6e76c8987ff41a762523b8f64876ba406d8a831d268ee0b63f1369582"


def post_install(self):
    self.install_license("COPYING")


@subpackage("quazip-devel")
def _(self):
    return self.default_devel()
