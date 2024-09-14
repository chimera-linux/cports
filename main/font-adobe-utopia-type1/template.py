pkgname = "font-adobe-utopia-type1"
pkgver = "1.0.5"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--with-mapfiles=/usr/share/fonts/util",
    "--with-fontdir=/usr/share/fonts/type1",
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
pkgdesc = "X.org adobe-utopia type1 font"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/font/font-adobe-utopia-type1-{pkgver}.tar.gz"
sha256 = "cd0b5acf8413d5a28afca6432c03ad0c9910fa707a38709bc9f235e9d7545e4d"


def post_install(self):
    self.install_license("COPYING")
