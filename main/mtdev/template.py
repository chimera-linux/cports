pkgname = "mtdev"
pkgver = "1.1.6"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
makedepends = ["linux-headers"]
pkgdesc = "Multitouch Protocol Translation Library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "http://bitmath.org/code/mtdev"
source = f"{url}/{pkgname}-{pkgver}.tar.bz2"
sha256 = "15d7b28da8ac71d8bc8c9287c2045fd174267bc740bec10cfda332dc1204e0e0"


def post_install(self):
    self.install_license("COPYING")


@subpackage("mtdev-devel")
def _devel(self):
    self.depends += ["linux-headers"]
    return self.default_devel()


configure_gen = []
