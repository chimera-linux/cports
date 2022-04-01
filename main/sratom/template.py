pkgname = "sratom"
pkgver = "0.6.8"
pkgrel = 0
build_style = "waf"
hostmakedepends = ["python", "pkgconf"]
makedepends = ["serd-devel", "sord-devel", "lv2"]
pkgdesc = "Library for serializing LV2 atoms to/from RDF"
maintainer = "q66 <q66@chimera-linux.org>"
license = "ISC"
url = "https://drobilla.net/software/sratom.html"
source = f"https://download.drobilla.net/{pkgname}-{pkgver}.tar.bz2"
sha256 = "3acb32b1adc5a2b7facdade2e0818bcd6c71f23f84a1ebc17815bb7a0d2d02df"
# FIXME check
options = ["!cross", "!check"]

def post_install(self):
    self.install_license("COPYING")

@subpackage("sratom-devel")
def _devel(self):
    return self.default_devel()
