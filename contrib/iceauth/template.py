pkgname = "iceauth"
pkgver = "1.0.9"
pkgrel = 1
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
makedepends = ["xorgproto", "libice-devel"]
pkgdesc = "ICE protocol utility"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/app/{pkgname}-{pkgver}.tar.gz"
sha256 = "5ca274cf210453e7d7cf5c827a2fbc92149df83824f99a27cde17e1f20324dc6"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")


configure_gen = []
