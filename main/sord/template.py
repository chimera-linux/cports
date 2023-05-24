pkgname = "sord"
pkgver = "0.16.14"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["serd-devel", "pcre2-devel"]
pkgdesc = "C library for storing RDF data in memory"
maintainer = "q66 <q66@chimera-linux.org>"
license = "ISC"
url = "https://drobilla.net/software/sord.html"
source = f"https://download.drobilla.net/{pkgname}-{pkgver}.tar.xz"
sha256 = "220fd97d5fcb216e7b85db66f685bfdaad7dc58a50d1f96dfb2558dbc6c4731b"
# FIXME cfi
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("sord-devel")
def _devel(self):
    return self.default_devel()


@subpackage("sord-progs")
def _progs(self):
    return self.default_progs()
