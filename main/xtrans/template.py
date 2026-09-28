pkgname = "xtrans"
pkgver = "1.6.0"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf", "automake", "xorg-util-macros"]
pkgdesc = "Network API translation layer to insulate X"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/xtrans-{pkgver}.tar.xz"
sha256 = "faafea166bf2451a173d9d593352940ec6404145c5d1da5c213423ce4d359e92"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")
