pkgname = "xbitmaps"
pkgver = "1.1.3"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
pkgdesc = "Common X11 bitmaps"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/data/{pkgname}-{pkgver}.tar.gz"
sha256 = "93b433b7ff223c4685fdba583b4bd30f2706be2413a670021084422d85b0269d"


def post_install(self):
    self.install_license("COPYING")


configure_gen = []
