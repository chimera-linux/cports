pkgname = "xlsfonts"
pkgver = "1.0.6"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
makedepends = ["libx11-devel"]
pkgdesc = "Server font list displayer for X"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/app/{pkgname}-{pkgver}.tar.bz2"
sha256 = "89b80b3a030006ab6cef717be286c12f2477894b227158b1e6133274f6ebd368"

def post_install(self):
    self.install_license("COPYING")
