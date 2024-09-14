pkgname = "font-bh-100dpi"
pkgver = "1.0.4"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--with-mapfiles=/usr/share/fonts/util",
    "--with-fontdir=/usr/share/fonts/100dpi",
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
pkgdesc = "X.org bh 100dpi font"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/font/font-bh-100dpi-{pkgver}.tar.gz"
sha256 = "cfd9b6bf6dae77eb7186afa296ad7233bb43d9c2f840d8010e197d55a2cc21dc"


def post_install(self):
    self.install_license("COPYING")
