pkgname = "libsm"
pkgver = "1.2.3"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
makedepends = ["libice-devel", "libuuid-devel", "xtrans"]
pkgdesc = "X session management library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/libSM-{pkgver}.tar.bz2"
sha256 = "2d264499dcb05f56438dee12a1b4b71d76736ce7ba7aa6efbf15ebb113769cbb"

def post_install(self):
    self.install_license("COPYING")

@subpackage("libsm-devel")
def _devel(self):
    return self.default_devel()
