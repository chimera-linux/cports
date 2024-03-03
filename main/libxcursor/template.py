pkgname = "libxcursor"
pkgver = "1.2.2"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "libtool", "pkgconf", "xorg-util-macros"]
makedepends = ["xorgproto", "libxfixes-devel", "libxrender-devel"]
pkgdesc = "Client-side cursor loading library for X"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/libXcursor-{pkgver}.tar.gz"
sha256 = "98c3a30a3f85274c167d1ac5419d681ce41f14e27bfa5fe3003c8172cd8af104"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libxcursor-devel")
def _devel(self):
    return self.default_devel()
