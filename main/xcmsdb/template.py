pkgname = "xcmsdb"
pkgver = "1.0.5"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
makedepends = ["libx11-devel"]
pkgdesc = "Device Color Characterization utility for X"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/app/{pkgname}-{pkgver}.tar.bz2"
sha256 = "e5585361bb8b6a05bb814a8d0e444ee93e0f00180881d3070aff4571e97f67c6"

def post_install(self):
    self.install_license("COPYING")
