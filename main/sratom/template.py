pkgname = "sratom"
pkgver = "0.6.12"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["serd-devel", "sord-devel", "lv2"]
pkgdesc = "Library for serializing LV2 atoms to/from RDF"
maintainer = "q66 <q66@chimera-linux.org>"
license = "ISC"
url = "https://drobilla.net/software/sratom.html"
source = f"https://download.drobilla.net/{pkgname}-{pkgver}.tar.xz"
sha256 = "349933ce75ee4b467f0d620defa5b2139a2194c16dbf11a837b5fa800c1a0c83"

def post_install(self):
    self.install_license("COPYING")

@subpackage("sratom-devel")
def _devel(self):
    return self.default_devel()
