pkgname = "libxtst"
pkgver = "1.2.5"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "libtool",
    "pkgconf",
    "xorg-util-macros",
]
makedepends = [
    "libxext-devel",
    "libxi-devel",
    "xorgproto",
]
pkgdesc = "X Tst library"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/libXtst-{pkgver}.tar.xz"
sha256 = "b50d4c25b97009a744706c1039c598f4d8e64910c9fde381994e1cae235d9242"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libxtst-devel")
def _(self):
    return self.default_devel()
