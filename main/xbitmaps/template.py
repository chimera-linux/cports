pkgname = "xbitmaps"
pkgver = "1.1.3"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = []
hostmakedepends = ["pkgconf"]
pkgdesc = "Common X11 bitmaps"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/data/xbitmaps-{pkgver}.tar.gz"
sha256 = "93b433b7ff223c4685fdba583b4bd30f2706be2413a670021084422d85b0269d"


def post_install(self):
    self.install_license("COPYING")
