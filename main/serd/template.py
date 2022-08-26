pkgname = "serd"
pkgver = "0.30.14"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
pkgdesc = "C library for RDF syntax"
maintainer = "q66 <q66@chimera-linux.org>"
license = "ISC"
url = "https://drobilla.net/software/serd.html"
source = f"https://download.drobilla.net/{pkgname}-{pkgver}.tar.xz"
sha256 = "a14137d47b11d6ad431e78da341ca9737998d9eaccf6a49263d4c8d79fd856e3"

def post_install(self):
    self.install_license("COPYING")

@subpackage("serd-devel")
def _devel(self):
    return self.default_devel()

@subpackage("serd-progs")
def _progs(self):
    return self.default_progs()
