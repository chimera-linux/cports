pkgname = "font-screen-cyrillic"
pkgver = "1.0.5"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--with-mapfiles=/usr/share/fonts/util",
    "--with-fontdir=/usr/share/fonts/cyrillic",
]
make_install_args = ["MKFONTDIR=:", "MKFONTSCALE=:", "FCCACHE=:"]
hostmakedepends = [
    "automake",
    "bdftopcf",
    "font-util-devel",
    "pkgconf",
    "xorg-util-macros",
]
depends = ["encodings", "font-alias", "mkfontscale"]
pkgdesc = "X.org screen cyrillic font"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/font/font-screen-cyrillic-{pkgver}.tar.gz"
sha256 = "c37615f4969b11d1c6f3cf4d78e0fc67d42d5fb5be30e0fe22a45f044ac8f62e"


def post_install(self):
    self.install_license("COPYING")
