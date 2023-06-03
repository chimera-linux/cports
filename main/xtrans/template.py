pkgname = "xtrans"
pkgver = "1.5.0"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf", "automake", "xorg-util-macros"]
pkgdesc = "Network API translation layer to insulate X"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/{pkgname}-{pkgver}.tar.gz"
sha256 = "a806f8a92f879dcd0146f3f1153fdffe845f2fc0df9b1a26c19312b7b0a29c86"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")
