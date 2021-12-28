pkgname = "libxdmcp"
pkgver = "1.1.3"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
makedepends = ["xorgproto"]
pkgdesc = "X Display Manager Control Protocol library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/libXdmcp-{pkgver}.tar.bz2"
sha256 = "20523b44aaa513e17c009e873ad7bbc301507a3224c232610ce2e099011c6529"

def post_install(self):
    self.install_license("COPYING")

@subpackage("libxdmcp-devel")
def _devel(self):
    return self.default_devel()
