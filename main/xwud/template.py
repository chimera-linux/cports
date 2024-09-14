pkgname = "xwud"
pkgver = "1.0.6"
pkgrel = 1
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
makedepends = ["libx11-devel"]
pkgdesc = "X image displayer"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/app/xwud-{pkgver}.tar.gz"
sha256 = "262171b0c434966ddbbe8a54afb9615567ad74d4cc2e823e14e51e099ec3ab0d"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")


configure_gen = []
