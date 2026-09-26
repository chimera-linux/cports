pkgname = "setxkbmap"
pkgver = "1.3.5"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = []
hostmakedepends = ["pkgconf"]
makedepends = ["libx11-devel", "libxkbfile-devel", "libxrandr-devel"]
pkgdesc = "Sets the X keyboard layout"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/app/setxkbmap-{pkgver}.tar.gz"
sha256 = "fe5948c40209b2ae35651968566cd09723865bf86a10a27b1e2ce3c6c543dd31"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")
