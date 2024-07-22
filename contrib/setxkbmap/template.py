pkgname = "setxkbmap"
pkgver = "1.3.4"
pkgrel = 1
build_style = "gnu_configure"
configure_gen = []
hostmakedepends = ["pkgconf"]
makedepends = ["libx11-devel", "libxkbfile-devel", "libxrandr-devel"]
pkgdesc = "Sets the X keyboard layout"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/app/setxkbmap-{pkgver}.tar.gz"
sha256 = "cc4113eab3cd70c28c986174aa30e62690e789723c874acc53e8d1f058d11f92"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")
