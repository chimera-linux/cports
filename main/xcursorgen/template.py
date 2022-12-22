pkgname = "xcursorgen"
pkgver = "1.0.7"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
makedepends = [
    "libx11-devel", "libxcursor-devel", "libxrender-devel",
    "libxfixes-devel", "libpng-devel"
]
pkgdesc = "X cursor generator"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/app/{pkgname}-{pkgver}.tar.bz2"
sha256 = "35b6f844b24f1776e9006c880a745728800764dbe3b327a128772b4610d8eb3d"

def post_install(self):
    self.install_license("COPYING")

# FIXME visibility
hardening = ["!vis"]
