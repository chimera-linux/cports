pkgname = "font-bh-lucidatypewriter-100dpi"
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
pkgdesc = "X.org bh-lucidatypewriter 100dpi font"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/font/font-bh-lucidatypewriter-100dpi-{pkgver}.tar.gz"
sha256 = "28dbf07022e608ecca198dfee9455a33bf1efa1323936a853b894515fbb4992a"


def post_install(self):
    self.install_license("COPYING")
