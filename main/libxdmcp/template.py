pkgname = "libxdmcp"
pkgver = "1.1.5"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "libtool", "pkgconf", "xorg-util-macros"]
makedepends = ["xorgproto"]
pkgdesc = "X Display Manager Control Protocol library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/libXdmcp-{pkgver}.tar.gz"
sha256 = "31a7abc4f129dcf6f27ae912c3eedcb94d25ad2e8f317f69df6eda0bc4e4f2f3"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libxdmcp-devel")
def _devel(self):
    return self.default_devel()
