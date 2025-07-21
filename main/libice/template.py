pkgname = "libice"
pkgver = "1.1.2"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "libtool",
    "pkgconf",
    "xorg-util-macros",
    "xtrans",
]
makedepends = ["xorgproto", "xtrans"]
pkgdesc = "Inter Client Exchange (ICE) library for X"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/libICE-{pkgver}.tar.gz"
sha256 = "1da62f732f8679c20045708a29372b82dff9e7eceee543ed488b845002b3b0ff"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libice-devel")
def _(self):
    return self.default_devel()
