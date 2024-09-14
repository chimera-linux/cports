pkgname = "xev"
pkgver = "1.2.6"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "pkgconf", "xorg-util-macros"]
makedepends = ["libxrandr-devel"]
pkgdesc = "Display X events"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/app/xev-{pkgver}.tar.gz"
sha256 = "e2e3527023017af3a9bfbef0a90f8e46ac354c506b51f0ee3834b30823e43b25"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")
