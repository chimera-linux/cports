pkgname = "libxcursor"
pkgver = "1.2.3"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "libtool", "pkgconf", "xorg-util-macros"]
makedepends = ["xorgproto", "libxfixes-devel", "libxrender-devel"]
pkgdesc = "Client-side cursor loading library for X"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/libXcursor-{pkgver}.tar.gz"
sha256 = "74e72da27e61cc2cfd2e267c14f500ea47775850048ee0b00362a55c9b60ee9b"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libxcursor-devel")
def _(self):
    return self.default_devel()
