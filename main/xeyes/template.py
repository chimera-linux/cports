pkgname = "xeyes"
pkgver = "1.2.0"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf", "xorg-util-macros"]
makedepends = ["libxmu-devel", "libxt-devel", "libxrender-devel", "libxi-devel"]
pkgdesc = "Follow the mouse"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/app/{pkgname}-{pkgver}.tar.bz2"
sha256 = "f8a17e23146bef1ab345a1e303c6749e42aaa7bcf4f25428afad41770721b6db"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")


configure_gen = []
