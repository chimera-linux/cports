pkgname = "libuninameslist"
pkgver = "20240524"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf", "automake", "libtool"]
pkgdesc = "Library of Unicode names and annotation data"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://github.com/fontforge/libuninameslist"
source = f"{url}/releases/download/{pkgver}/{pkgname}-dist-{pkgver}.tar.gz"
sha256 = "cb69d6b0b1bf896c98cd00497d3078be2d22b896b0dc7cba2bb3d6bc3172dac5"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libuninameslist-devel")
def _devel(self):
    return self.default_devel()
