pkgname = "libxdmcp"
pkgver = "1.1.4"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
makedepends = ["xorgproto"]
pkgdesc = "X Display Manager Control Protocol library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/libXdmcp-{pkgver}.tar.gz"
sha256 = "55041a8ff8992ab02777478c4b19c249c0f8399f05a752cb4a1a868a9a0ccb9a"

def post_install(self):
    self.install_license("COPYING")

@subpackage("libxdmcp-devel")
def _devel(self):
    return self.default_devel()

configure_gen = []
