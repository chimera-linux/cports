pkgname = "libxdamage"
pkgver = "1.1.6"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "pkgconf", "slibtool", "xorg-util-macros"]
makedepends = ["xorgproto", "libxfixes-devel"]
pkgdesc = "Xdamage extension Library"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/libXdamage-{pkgver}.tar.gz"
sha256 = "2afcc139eb6eb926ffe344494b1fc023da25def42874496e6e6d3aa8acef8595"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libxdamage-devel")
def _(self):
    return self.default_devel()
