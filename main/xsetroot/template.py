pkgname = "xsetroot"
pkgver = "1.1.2"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
makedepends = [
    "xbitmaps", "libxmu-devel", "libxrender-devel",
    "libxfixes-devel", "libxcursor-devel"
]
pkgdesc = "X root window parameter setting utility"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/app/{pkgname}-{pkgver}.tar.bz2"
sha256 = "10c442ba23591fb5470cea477a0aa5f679371f4f879c8387a1d9d05637ae417c"

def post_install(self):
    self.install_license("COPYING")
