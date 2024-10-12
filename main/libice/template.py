pkgname = "libice"
pkgver = "1.1.1"
pkgrel = 1
build_style = "gnu_configure"
hostmakedepends = [
    "pkgconf",
    "automake",
    "libtool",
    "xorg-util-macros",
    "xtrans",
]
makedepends = ["xorgproto", "xtrans"]
pkgdesc = "Inter Client Exchange (ICE) library for X"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/libICE-{pkgver}.tar.gz"
sha256 = "04fbd34a11ba08b9df2e3cdb2055c2e3c1c51b3257f683d7fcf42dabcf8e1210"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libice-devel")
def _(self):
    return self.default_devel()
