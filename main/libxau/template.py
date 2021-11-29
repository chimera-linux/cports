pkgname = "libxau"
pkgver = "1.0.9"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
makedepends = ["xorgproto"]
pkgdesc = "Authorization Protocol for X"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/libXau-{pkgver}.tar.bz2"
sha256 = "ccf8cbf0dbf676faa2ea0a6d64bcc3b6746064722b606c8c52917ed00dcb73ec"

def post_install(self):
    self.install_license("COPYING")

@subpackage("libxau-static")
def _static(self):
    return self.default_static()

@subpackage("libxau-devel")
def _devel(self):
    return self.default_devel()
