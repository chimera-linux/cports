pkgname = "libxmu"
pkgver = "1.2.1"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "libtool", "pkgconf", "xorg-util-macros"]
makedepends = ["xorgproto", "libxext-devel", "libxt-devel"]
pkgdesc = "X Miscellaneous Utilities library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/libXmu-{pkgver}.tar.gz"
sha256 = "bf0902583dd1123856c11e0a5085bd3c6e9886fbbd44954464975fd7d52eb599"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libxmu-devel")
def _devel(self):
    return self.default_devel()
