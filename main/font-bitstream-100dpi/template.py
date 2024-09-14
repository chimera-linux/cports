pkgname = "font-bitstream-100dpi"
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
pkgdesc = "X.org bitstream 100dpi font"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/font/font-bitstream-100dpi-{pkgver}.tar.gz"
sha256 = "1d4b38aaf700b13c17c5d7c7816a1abe7edf8fcfd5b584fc619d42b13a10e751"


def post_install(self):
    self.install_license("COPYING")
