pkgname = "transset"
pkgver = "1.0.2"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
makedepends = ["libxt-devel"]
pkgdesc = "Sets the transparency of an X window"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/app/{pkgname}-{pkgver}.tar.bz2"
sha256 = "4bac142ee7cfda574893b2f6b4e413dacd88a130c6dca5be1a9958e7c1451b21"

def post_install(self):
    self.install_license("COPYING")
