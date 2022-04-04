pkgname = "sord"
pkgver = "0.16.8"
pkgrel = 0
build_style = "waf"
configure_args = ["--test"]
hostmakedepends = ["python", "pkgconf"]
makedepends = ["serd-devel", "pcre-devel"]
pkgdesc = "C library for storing RDF data in memory"
maintainer = "q66 <q66@chimera-linux.org>"
license = "ISC"
url = "https://drobilla.net/software/sord.html"
source = f"https://download.drobilla.net/{pkgname}-{pkgver}.tar.bz2"
sha256 = "7c289d2eaabf82fa6ac219107ce632d704672dcfb966e1a7ff0bbc4ce93f5e14"
options = ["!cross"]

def post_install(self):
    self.install_license("COPYING")

@subpackage("sord-devel")
def _devel(self):
    return self.default_devel()

@subpackage("sord-progs")
def _progs(self):
    return self.default_progs()
