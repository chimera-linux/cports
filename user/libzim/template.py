pkgname = "libzim"
pkgver = "9.8.2"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Ddoc=false",
    "-Dexamples=false",
    "-Dtests=false",
    "-Dwith_xapian=true",
    "-Dwerror=false",
]
hostmakedepends = [
    "meson",
    "ninja",
    "pkgconf",
]
makedepends = [
    "icu-devel",
    "xapian-core-devel",
    "xz-devel",
    "zstd-devel",
]
pkgdesc = "Reference implementation of the ZIM file format"
license = "GPL-2.0-or-later"
url = "https://github.com/openzim/libzim"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "38f8e2139a089f00196f288f52f2d0677a6becc218f380b54ca70b6f162398bd"
# tests require external ZIM test data
options = ["!check"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("libzim-devel")
def _(self):
    return self.default_devel()
