pkgname = "xprop"
pkgver = "1.2.5"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
makedepends = ["libx11-devel", "libxmu-devel"]
pkgdesc = "X property displayer"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/app/{pkgname}-{pkgver}.tar.bz2"
sha256 = "9b92ed0316bf2486121d8bac88bd1878f16b43bd335f18009b1f941f1eca93a1"

def post_install(self):
    self.install_license("COPYING")
