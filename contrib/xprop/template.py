pkgname = "xprop"
pkgver = "1.2.7"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "pkgconf", "xorg-util-macros"]
makedepends = ["libx11-devel", "libxmu-devel"]
pkgdesc = "X property displayer"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/app/{pkgname}-{pkgver}.tar.gz"
sha256 = "11c06a876b0aa0bfac6cbfe4b3ebe1f5062f8b39b9b1b6c136a8629265f134b6"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")
