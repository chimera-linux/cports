pkgname = "xprop"
pkgver = "1.2.8"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "pkgconf", "xorg-util-macros"]
makedepends = ["libx11-devel", "libxmu-devel"]
pkgdesc = "X property displayer"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/app/xprop-{pkgver}.tar.gz"
sha256 = "a8394338c99775160d733d54d73cdcdc5c9c80a0dc8cffd5be1b7c977254b745"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")
