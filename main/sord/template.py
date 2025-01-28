pkgname = "sord"
pkgver = "0.16.18"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["serd-devel", "pcre2-devel", "zix-devel"]
pkgdesc = "C library for storing RDF data in memory"
maintainer = "q66 <q66@chimera-linux.org>"
license = "ISC"
url = "https://drobilla.net/software/sord.html"
source = f"https://download.drobilla.net/sord-{pkgver}.tar.xz"
sha256 = "4f398b635894491a4774b1498959805a08e11734c324f13d572dea695b13d3b3"
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("sord-devel")
def _(self):
    return self.default_devel()


@subpackage("sord-progs")
def _(self):
    return self.default_progs()
