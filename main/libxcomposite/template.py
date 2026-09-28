pkgname = "libxcomposite"
pkgver = "0.4.7"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "pkgconf", "slibtool", "xorg-util-macros"]
makedepends = ["xorgproto", "libxfixes-devel"]
pkgdesc = "X Composite library"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/libXcomposite-{pkgver}.tar.gz"
sha256 = "5fc39a8fd6452ec225a95070dd5ac312899247a154fd041cc5f100a93c4ce192"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libxcomposite-devel")
def _(self):
    return self.default_devel()
