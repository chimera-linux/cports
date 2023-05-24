pkgname = "serd"
pkgver = "0.30.16"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
pkgdesc = "C library for RDF syntax"
maintainer = "q66 <q66@chimera-linux.org>"
license = "ISC"
url = "https://drobilla.net/software/serd.html"
source = f"https://download.drobilla.net/{pkgname}-{pkgver}.tar.xz"
sha256 = "f50f486da519cdd8d03b20c9e42414e459133f5a244411d8e63caef8d9ac9146"
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
