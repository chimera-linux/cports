pkgname = "xtrans"
pkgver = "1.4.0"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf", "automake", "xorg-util-macros"]
pkgdesc = "Network API translation layer to insulate X"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/{pkgname}-{pkgver}.tar.bz2"
sha256 = "377c4491593c417946efcd2c7600d1e62639f7a8bbca391887e2c4679807d773"
hardening = ["vis", "cfi"]

def post_install(self):
    self.install_license("COPYING")
