pkgname = "libuninameslist"
pkgver = "20230523"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf", "automake", "libtool"]
pkgdesc = "Library of Unicode names and annotation data"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://github.com/fontforge/libuninameslist"
source = f"{url}/releases/download/{pkgver}/{pkgname}-dist-{pkgver}.tar.gz"
sha256 = "d52f9187f250984b48ac8af3db4efd46177eb28a65826d96216af71153a8a1f9"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libuninameslist-devel")
def _devel(self):
    return self.default_devel()
