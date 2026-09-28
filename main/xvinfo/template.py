pkgname = "xvinfo"
pkgver = "1.1.6"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "pkgconf", "xorg-util-macros"]
makedepends = ["libxv-devel"]
pkgdesc = "X video capabilities query utility"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/app/xvinfo-{pkgver}.tar.gz"
sha256 = "1462820e914432e08afd64379bf9d4e8a3c7a71ecebbbd70756f9a2fbc263478"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")
