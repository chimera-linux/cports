pkgname = "font-arabic-misc"
pkgver = "1.0.4"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--with-mapfiles=/usr/share/fonts/util",
    "--with-fontdir=/usr/share/fonts/misc",
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
pkgdesc = "X.org arabic misc font"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/font/font-arabic-misc-{pkgver}.tar.gz"
sha256 = "ea2c69a5e3e9210eca2c12a48f74f5ea24d9c0d9ba7d46bbd30b0a1a338e37e5"


def post_install(self):
    self.install_license("COPYING")
