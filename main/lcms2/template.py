pkgname = "lcms2"
pkgver = "2.14"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
makedepends = ["libtiff-devel"]
pkgdesc = "Small-footprint color management engine"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://littlecms.com"
source = f"$(SOURCEFORGE_SITE)/lcms/{pkgname}-{pkgver}.tar.gz"
sha256 = "28474ea6f6591c4d4cee972123587001a4e6e353412a41b3e9e82219818d5740"
# FIXME cfi
hardening = ["vis", "!cfi"]

def post_install(self):
    self.install_license("COPYING")

@subpackage("lcms2-devel")
def _devel(self):
    self.depends += makedepends

    return self.default_devel()

@subpackage("lcms2-progs")
def _progs(self):
    return self.default_progs()
