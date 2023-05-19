pkgname = "xlsfonts"
pkgver = "1.0.7"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
makedepends = ["libx11-devel"]
pkgdesc = "Server font list displayer for X"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/app/{pkgname}-{pkgver}.tar.gz"
sha256 = "b92d4954eaf525674ff83f7e85240ef166c240a774277f71c30674f9f7794171"
hardening = ["vis", "cfi"]

def post_install(self):
    self.install_license("COPYING")

configure_gen = []
