pkgname = "xcursorgen"
pkgver = "1.0.8"
pkgrel = 1
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
makedepends = [
    "libx11-devel",
    "libxcursor-devel",
    "libxrender-devel",
    "libxfixes-devel",
    "libpng-devel",
]
pkgdesc = "X cursor generator"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/app/xcursorgen-{pkgver}.tar.gz"
sha256 = "b8bb2756918343b8bc15a4ce875e9efb6c4e7777adba088280e53dd09753b6ac"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")


configure_gen = []
