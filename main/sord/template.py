pkgname = "sord"
pkgver = "0.16.16"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["serd-devel", "pcre2-devel", "zix-devel"]
pkgdesc = "C library for storing RDF data in memory"
maintainer = "q66 <q66@chimera-linux.org>"
license = "ISC"
url = "https://drobilla.net/software/sord.html"
source = f"https://download.drobilla.net/{pkgname}-{pkgver}.tar.xz"
sha256 = "257f876d756143da02ee84c9260af93559d6249dd87f317e70ab5fffcc975fd0"
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
