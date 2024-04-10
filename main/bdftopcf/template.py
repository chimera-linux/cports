pkgname = "bdftopcf"
pkgver = "1.1.1"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "pkgconf", "xorg-util-macros"]
makedepends = ["xorgproto"]
pkgdesc = "BDF to PCF font converter"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/util/{pkgname}-{pkgver}.tar.xz"
sha256 = "11c953d53c0f3ed349d0198dfb0a40000b5121df7eef09f2615a262892fed908"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")
