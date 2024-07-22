pkgname = "font-misc-misc"
pkgver = "1.1.3"
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
pkgdesc = "X.org misc misc font"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/font/font-misc-misc-{pkgver}.tar.gz"
sha256 = "bece4a9482b3cb6f7fad2164fd3b394d22dfe1ad2f96f60030a703bcff30f5a5"


def post_install(self):
    self.install_license("COPYING")
