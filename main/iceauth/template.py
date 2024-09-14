pkgname = "iceauth"
pkgver = "1.0.10"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "pkgconf", "xorg-util-macros"]
makedepends = ["xorgproto", "libice-devel"]
pkgdesc = "ICE protocol utility"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/app/iceauth-{pkgver}.tar.gz"
sha256 = "f17f373c6e7bfef9cfa4c688f165dfebec7642ad7c6304c5bb3c9bc2bfcde747"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")
