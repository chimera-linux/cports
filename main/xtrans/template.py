pkgname = "xtrans"
pkgver = "1.5.2"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf", "automake", "xorg-util-macros"]
pkgdesc = "Network API translation layer to insulate X"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/xtrans-{pkgver}.tar.xz"
sha256 = "5c5cbfe34764a9131d048f03c31c19e57fb4c682d67713eab6a65541b4dff86c"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")
