pkgname = "bdftopcf"
pkgver = "1.1.2"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "pkgconf", "xorg-util-macros"]
makedepends = ["xorgproto"]
pkgdesc = "BDF to PCF font converter"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/util/bdftopcf-{pkgver}.tar.xz"
sha256 = "bc60be5904330faaa3ddd2aed7874bee2f29e4387c245d6787552f067eb0523a"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")
