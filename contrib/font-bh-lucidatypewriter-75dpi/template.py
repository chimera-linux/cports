pkgname = "font-bh-lucidatypewriter-75dpi"
pkgver = "1.0.4"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--with-mapfiles=/usr/share/fonts/util",
    "--with-fontdir=/usr/share/fonts/75dpi",
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
pkgdesc = "X.org bh-lucidatypewriter 75dpi font"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/font/font-bh-lucidatypewriter-75dpi-{pkgver}.tar.gz"
sha256 = "8e502a1a7e81c1b95f08725f40e7e137d4d06700794d006b327d54b7c8d07f88"


def post_install(self):
    self.install_license("COPYING")
