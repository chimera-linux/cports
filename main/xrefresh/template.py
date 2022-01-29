pkgname = "xrefresh"
pkgver = "1.0.6"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
makedepends = ["libx11-devel"]
pkgdesc = "Refresh all or a part of an X screen"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/app/{pkgname}-{pkgver}.tar.bz2"
sha256 = "287dfb9bb7e8d780d07e672e3252150850869cb550958ed5f8401f0835cd6353"

def post_install(self):
    self.install_license("COPYING")
