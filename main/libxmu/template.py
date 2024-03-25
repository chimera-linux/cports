pkgname = "libxmu"
pkgver = "1.2.0"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "libtool", "pkgconf", "xorg-util-macros"]
makedepends = ["xorgproto", "libxext-devel", "libxt-devel"]
pkgdesc = "X Miscellaneous Utilities library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/libXmu-{pkgver}.tar.gz"
sha256 = "b4686c4b4570044bcfc35bfaa3edbe68185ddf8e3250387f74a140c8e45afb2f"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libxmu-devel")
def _devel(self):
    return self.default_devel()
