pkgname = "sratom"
pkgver = "0.6.22"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["serd-devel", "sord-devel", "lv2"]
pkgdesc = "Library for serializing LV2 atoms to/from RDF"
license = "ISC"
url = "https://drobilla.net/software/sratom.html"
source = f"https://download.drobilla.net/sratom-{pkgver}.tar.xz"
sha256 = "0209b7d0f22c96abb416722ed735b0933be47931ecff4aa4b26ded7760b4f252"
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("sratom-devel")
def _(self):
    return self.default_devel()
