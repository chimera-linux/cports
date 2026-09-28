pkgname = "xeyes"
pkgver = "1.3.1"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "pkgconf", "xorg-util-macros"]
makedepends = ["libxmu-devel", "libxt-devel", "libxrender-devel", "libxi-devel"]
pkgdesc = "Follow the mouse"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/app/xeyes-{pkgver}.tar.gz"
sha256 = "d223283270488b1a6b408d0e97bd69a7704cf6a9596c0320035d807e63cdc084"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")
