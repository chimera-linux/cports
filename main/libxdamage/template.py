pkgname = "libxdamage"
pkgver = "1.1.5"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
makedepends = ["xorgproto", "libxfixes-devel"]
pkgdesc = "Xdamage extension Library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/libXdamage-{pkgver}.tar.bz2"
sha256 = "b734068643cac3b5f3d2c8279dd366b5bf28c7219d9e9d8717e1383995e0ea45"

def post_install(self):
    self.install_license("COPYING")

@subpackage("libxdamage-static")
def _static(self):
    return self.default_static()

@subpackage("libxdamage-devel")
def _devel(self):
    return self.default_devel()
