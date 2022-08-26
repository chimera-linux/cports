pkgname = "sord"
pkgver = "0.16.12"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["serd-devel", "pcre-devel"]
pkgdesc = "C library for storing RDF data in memory"
maintainer = "q66 <q66@chimera-linux.org>"
license = "ISC"
url = "https://drobilla.net/software/sord.html"
source = f"https://download.drobilla.net/{pkgname}-{pkgver}.tar.xz"
sha256 = "fde269893cb24b2ab7b75708d7a349c6e760c47a0d967aeca5b1c651294ff9f2"

def post_install(self):
    self.install_license("COPYING")

@subpackage("sord-devel")
def _devel(self):
    return self.default_devel()

@subpackage("sord-progs")
def _progs(self):
    return self.default_progs()
