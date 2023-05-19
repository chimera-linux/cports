pkgname = "xkbcomp"
pkgver = "1.4.6"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf", "bison"]
makedepends = ["libx11-devel", "libxkbfile-devel"]
pkgdesc = "XKBD keymap compiler"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/app/{pkgname}-{pkgver}.tar.gz"
sha256 = "b216a2c8c0eab83f3dc4a3d5ee2bdf7827b30e49c8907035d0f222138eca0987"
hardening = ["vis", "cfi"]

def post_install(self):
    self.install_license("COPYING")

configure_gen = []
