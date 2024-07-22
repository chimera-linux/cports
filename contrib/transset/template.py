pkgname = "transset"
pkgver = "1.0.3"
pkgrel = 1
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
makedepends = ["libxt-devel"]
pkgdesc = "Sets the transparency of an X window"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/app/transset-{pkgver}.tar.gz"
sha256 = "adba0da81dacdebe5275ec0117dd08685e4f2f31afa0391f423e54906d0fb824"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")


configure_gen = []
