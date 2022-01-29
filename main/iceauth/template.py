pkgname = "iceauth"
pkgver = "1.0.8"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
makedepends = ["xorgproto", "libice-devel"]
pkgdesc = "ICE protocol utility"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/app/{pkgname}-{pkgver}.tar.bz2"
sha256 = "e6ee213a217265cc76050e4293ea70b98c32dce6505c6421227efbda62ab60c6"

def post_install(self):
    self.install_license("COPYING")
