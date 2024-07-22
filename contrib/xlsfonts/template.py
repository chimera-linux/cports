pkgname = "xlsfonts"
pkgver = "1.0.8"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "pkgconf", "xorg-util-macros"]
makedepends = ["libx11-devel"]
pkgdesc = "Server font list displayer for X"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/app/xlsfonts-{pkgver}.tar.gz"
sha256 = "448ba05919bafc6b2ca3d21982646b060e2af3a27a5cc05fcedbe8b2608388cb"
# FIXME: int
hardening = ["vis", "cfi", "!int"]


def post_install(self):
    self.install_license("COPYING")
