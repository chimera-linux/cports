pkgname = "xlsatoms"
pkgver = "1.1.3"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
makedepends = ["libxcb-devel"]
pkgdesc = "List interned atoms defined on the X server"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/app/{pkgname}-{pkgver}.tar.bz2"
sha256 = "57868f958c263976727881f3078e55b86b4a109dc578d2b92f5c6d690850a382"

def post_install(self):
    self.install_license("COPYING")
