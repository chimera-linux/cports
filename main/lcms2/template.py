pkgname = "lcms2"
pkgver = "2.13.1"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
makedepends = ["libtiff-devel"]
pkgdesc = "Small-footprint color management engine"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://littlecms.com"
source = f"$(SOURCEFORGE_SITE)/lcms/{pkgname}-{pkgver}.tar.gz"
sha256 = "d473e796e7b27c5af01bd6d1552d42b45b43457e7182ce9903f38bb748203b88"

def post_install(self):
    self.install_license("COPYING")

@subpackage("lcms2-devel")
def _devel(self):
    self.depends += makedepends

    return self.default_devel()

@subpackage("lcms2-progs")
def _progs(self):
    return self.default_progs()
