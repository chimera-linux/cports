pkgname = "font-adobe-utopia-100dpi"
pkgver = "1.0.5"
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
pkgdesc = "X.org adobe-utopia 100dpi font"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/font/font-adobe-utopia-100dpi-{pkgver}.tar.gz"
sha256 = "1a67e926dc13e46181ad6106dc0cdc4d1767500865444709dc28e9262a640f4f"


def post_install(self):
    self.install_license("COPYING")
