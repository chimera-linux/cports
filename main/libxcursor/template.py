pkgname = "libxcursor"
pkgver = "1.2.1"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
makedepends = ["xorgproto", "libxfixes-devel", "libxrender-devel"]
pkgdesc = "Client-side cursor loading library for X"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/libXcursor-{pkgver}.tar.gz"
sha256 = "77f96b9ad0a3c422cfa826afabaf1e02b9bfbfc8908c5fa1a45094faad074b98"

def post_install(self):
    self.install_license("COPYING")

@subpackage("libxcursor-devel")
def _devel(self):
    return self.default_devel()

configure_gen = []
