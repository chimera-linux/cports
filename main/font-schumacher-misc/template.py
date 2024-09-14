pkgname = "font-schumacher-misc"
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
pkgdesc = "X.org schumacher misc font"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/font/font-schumacher-misc-{pkgver}.tar.gz"
sha256 = "0a330ec905ef083af1b740a355b548aef75997f29d3169ef9dba76514b196893"


def post_install(self):
    self.install_license("COPYING")
