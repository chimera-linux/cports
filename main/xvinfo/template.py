pkgname = "xvinfo"
pkgver = "1.1.4"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
makedepends = ["libxv-devel"]
pkgdesc = "X video capabilities query utility"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/app/{pkgname}-{pkgver}.tar.bz2"
sha256 = "0353220d6606077ba42363db65f50410759f9815352f77adc799e2adfa76e73f"

def post_install(self):
    self.install_license("COPYING")

# FIXME visibility
hardening = ["!vis"]
