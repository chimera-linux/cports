pkgname = "xlsclients"
pkgver = "1.1.4"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
makedepends = ["libxcb-devel"]
pkgdesc = "X client listing utility"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/app/{pkgname}-{pkgver}.tar.bz2"
sha256 = "773f2af49c7ea2c44fba4213bee64325875c1b3c9bc4bbcd8dac9261751809c1"

def post_install(self):
    self.install_license("COPYING")
