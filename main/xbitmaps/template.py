pkgname = "xbitmaps"
pkgver = "1.1.2"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
pkgdesc = "Common X11 bitmaps"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/data/{pkgname}-{pkgver}.tar.bz2"
sha256 = "b9f0c71563125937776c8f1f25174ae9685314cbd130fb4c2efce811981e07ee"

def post_install(self):
    self.install_license("COPYING")
