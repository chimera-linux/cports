pkgname = "sratom"
pkgver = "0.6.14"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["serd-devel", "sord-devel", "lv2"]
pkgdesc = "Library for serializing LV2 atoms to/from RDF"
maintainer = "q66 <q66@chimera-linux.org>"
license = "ISC"
url = "https://drobilla.net/software/sratom.html"
source = f"https://download.drobilla.net/{pkgname}-{pkgver}.tar.xz"
sha256 = "9982faf40db83aedd9b3850e499fecd6852b8b4ba6dede514013655cffaca1e6"
# FIXME cfi
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("sratom-devel")
def _devel(self):
    return self.default_devel()
