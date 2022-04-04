pkgname = "serd"
pkgver = "0.30.10"
pkgrel = 0
build_style = "waf"
configure_args = ["--test"]
hostmakedepends = ["python", "pkgconf"]
pkgdesc = "C library for RDF syntax"
maintainer = "q66 <q66@chimera-linux.org>"
license = "ISC"
url = "https://drobilla.net/software/serd.html"
source = f"https://download.drobilla.net/{pkgname}-{pkgver}.tar.bz2"
sha256 = "affa80deec78921f86335e6fc3f18b80aefecf424f6a5755e9f2fa0eb0710edf"
options = ["!cross"]

def post_install(self):
    self.install_license("COPYING")

@subpackage("serd-devel")
def _devel(self):
    return self.default_devel()

@subpackage("serd-progs")
def _progs(self):
    return self.default_progs()
