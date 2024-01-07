pkgname = "libuninameslist"
pkgver = "20230916"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf", "automake", "libtool"]
pkgdesc = "Library of Unicode names and annotation data"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://github.com/fontforge/libuninameslist"
source = f"{url}/releases/download/{pkgver}/{pkgname}-dist-{pkgver}.tar.gz"
sha256 = "3ce49721de808a389f90997e9217adac449ab23e2fbf2115b22a8664e0e0a686"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libuninameslist-devel")
def _devel(self):
    return self.default_devel()
