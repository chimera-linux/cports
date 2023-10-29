pkgname = "serd"
pkgver = "0.32.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
pkgdesc = "C library for RDF syntax"
maintainer = "q66 <q66@chimera-linux.org>"
license = "ISC"
url = "https://drobilla.net/software/serd.html"
source = f"https://download.drobilla.net/{pkgname}-{pkgver}.tar.xz"
sha256 = "d1e8699468e01d2a76abe402b4d5c60c5095335c92b259088f062bdd3b929ca1"
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
