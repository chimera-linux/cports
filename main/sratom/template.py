pkgname = "sratom"
pkgver = "0.6.18"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["serd-devel", "sord-devel", "lv2"]
pkgdesc = "Library for serializing LV2 atoms to/from RDF"
maintainer = "q66 <q66@chimera-linux.org>"
license = "ISC"
url = "https://drobilla.net/software/sratom.html"
source = f"https://download.drobilla.net/sratom-{pkgver}.tar.xz"
sha256 = "4c6a6d9e0b4d6c01cc06a8849910feceb92e666cb38779c614dd2404a9931e92"
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("sratom-devel")
def _(self):
    return self.default_devel()
