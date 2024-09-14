pkgname = "xlsclients"
pkgver = "1.1.5"
pkgrel = 1
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
makedepends = ["libxcb-devel"]
pkgdesc = "X client listing utility"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/app/xlsclients-{pkgver}.tar.gz"
sha256 = "225d75e4c0b0929f16f974e20931ab85204b40098d92a5479b0b9379120637e5"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")


configure_gen = []
