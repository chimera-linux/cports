pkgname = "lcms2"
pkgver = "2.12"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
makedepends = ["libtiff-devel"]
pkgdesc = "Small-footprint color management engine"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://littlecms.com"
source = f"$(SOURCEFORGE_SITE)/lcms/{pkgname}-{pkgver}.tar.gz"
sha256 = "18663985e864100455ac3e507625c438c3710354d85e5cbb7cd4043e11fe10f5"

def post_install(self):
    self.install_license("COPYING")

@subpackage("lcms2-static")
def _static(self):
    return self.default_static()

@subpackage("lcms2-devel")
def _devel(self):
    self.depends += makedepends

    return self.default_devel()

@subpackage("lcms2-progs")
def _progs(self):
    return self.default_progs(man = True)
