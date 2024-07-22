pkgname = "font-misc-ethiopic"
pkgver = "1.0.5"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--with-mapfiles=/usr/share/fonts/util",
    "--with-fontdir=/usr/share/fonts/ethiopic",
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
pkgdesc = "X.org misc ethiopic font"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/font/font-misc-ethiopic-{pkgver}.tar.gz"
sha256 = "ce28324c3bb6258c6f138900cf35346d8cff0b9ffba2f5fbdbad7baa6a9691fd"


def post_install(self):
    self.install_license("COPYING")
