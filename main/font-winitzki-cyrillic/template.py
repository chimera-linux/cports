pkgname = "font-winitzki-cyrillic"
pkgver = "1.0.4"
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
pkgdesc = "X.org winitzki cyrillic font"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/font/font-winitzki-cyrillic-{pkgver}.tar.gz"
sha256 = "de3b63aae144093e32ee10087d807c4377a8bde2442f0c6a3df817fd47d54f54"


def post_install(self):
    self.install_license("COPYING")
