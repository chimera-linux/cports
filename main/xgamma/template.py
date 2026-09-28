pkgname = "xgamma"
pkgver = "1.0.8"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "pkgconf", "xorg-util-macros"]
makedepends = ["libx11-devel", "libxxf86vm-devel"]
pkgdesc = "X gamma utility"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/app/xgamma-{pkgver}.tar.gz"
sha256 = "96ab71ea6a6791538324bb4d2014627816d83178a0ac79335d8c9ef25ce59f1d"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")
