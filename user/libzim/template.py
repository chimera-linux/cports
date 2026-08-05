pkgname = "libzim"
pkgver = "9.6.0"
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
    "python",
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
sha256 = "a4211000de19df0a36dd48180b295be63adfbdaba3ef75545b32087c0bd8189d"
# tests require external ZIM test data
options = ["!check"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("libzim-devel")
def _(self):
    return self.default_devel()
