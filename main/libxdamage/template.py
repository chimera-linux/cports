pkgname = "libxdamage"
pkgver = "1.1.7"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "pkgconf", "slibtool", "xorg-util-macros"]
makedepends = ["xorgproto", "libxfixes-devel"]
pkgdesc = "Xdamage extension Library"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/libXdamage-{pkgver}.tar.gz"
sha256 = "fd5fcc94626886451b731cbcc500bdb3d5afd6d608056540b7cbc314c7678bfe"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libxdamage-devel")
def _(self):
    return self.default_devel()
