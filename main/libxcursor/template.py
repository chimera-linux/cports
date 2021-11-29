pkgname = "libxcursor"
pkgver = "1.2.0"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
makedepends = ["xorgproto", "libxfixes-devel", "libxrender-devel"]
pkgdesc = "Client-side cursor loading library for X"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/libXcursor-{pkgver}.tar.bz2"
sha256 = "3ad3e9f8251094af6fe8cb4afcf63e28df504d46bfa5a5529db74a505d628782"
options = ["lto"]

def post_install(self):
    self.install_license("COPYING")

@subpackage("libxcursor-static")
def _static(self):
    return self.default_static()

@subpackage("libxcursor-devel")
def _devel(self):
    return self.default_devel(extra = ["usr/share"])
