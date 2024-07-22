pkgname = "xgamma"
pkgver = "1.0.7"
pkgrel = 1
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
makedepends = ["libx11-devel", "libxxf86vm-devel"]
pkgdesc = "X gamma utility"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/app/xgamma-{pkgver}.tar.gz"
sha256 = "61f5ef02883d65ab464678ad3d8c5445a0ff727fe6255af90b1b842ddf77370d"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")


configure_gen = []
