pkgname = "libxcomposite"
pkgver = "0.4.5"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
makedepends = ["xorgproto", "libxfixes-devel"]
pkgdesc = "X Composite library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/libXcomposite-{pkgver}.tar.bz2"
sha256 = "b3218a2c15bab8035d16810df5b8251ffc7132ff3aa70651a1fba0bfe9634e8f"

def post_install(self):
    self.install_license("COPYING")

@subpackage("libxcomposite-static")
def _static(self):
    return self.default_static()

@subpackage("libxcomposite-devel")
def _devel(self):
    return self.default_devel(man = True)
