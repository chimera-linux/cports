pkgname = "libxpresent"
pkgver = "1.0.2"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "pkgconf", "slibtool", "xorg-util-macros"]
makedepends = ["xorgproto", "libxfixes-devel", "libxrandr-devel"]
pkgdesc = "XPresent extension library"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/libXpresent-{pkgver}.tar.gz"
sha256 = "e98a211e51d8b9381d16b24a57cecb926a23e743b9e0b1ffc3e870206b7dee1a"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libxpresent-devel")
def _(self):
    return self.default_devel()
