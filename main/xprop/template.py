pkgname = "xprop"
pkgver = "1.2.6"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
makedepends = ["libx11-devel", "libxmu-devel"]
pkgdesc = "X property displayer"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/app/{pkgname}-{pkgver}.tar.gz"
sha256 = "58ee5ee0c47fa454d3b16312e778c3f549605a8ad0fd0daafc70d2d6174b116d"
hardening = ["vis", "cfi"]

def post_install(self):
    self.install_license("COPYING")

configure_gen = []
