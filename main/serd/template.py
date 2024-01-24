pkgname = "serd"
pkgver = "0.32.2"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
pkgdesc = "C library for RDF syntax"
maintainer = "q66 <q66@chimera-linux.org>"
license = "ISC"
url = "https://drobilla.net/software/serd.html"
source = f"https://download.drobilla.net/{pkgname}-{pkgver}.tar.xz"
sha256 = "df7dc2c96f2ba1decfd756e458e061ded7d8158d255554e7693483ac0963c56b"
# FIXME cfi
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("serd-devel")
def _devel(self):
    return self.default_devel()


@subpackage("serd-progs")
def _progs(self):
    return self.default_progs()
