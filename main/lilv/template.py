pkgname = "lilv"
pkgver = "0.24.12"
pkgrel = 0
build_style = "waf"
configure_args = ["--test", "--dyn-manifest"]
hostmakedepends = ["python", "pkgconf"]
makedepends = [
    "libsndfile-devel", "python-devel", "serd-devel", "sord-devel",
    "sratom-devel", "lv2"
]
pkgdesc = "C API for using LV2 plugins"
maintainer = "q66 <q66@chimera-linux.org>"
license = "ISC"
url = "https://drobilla.net/software/lilv.html"
source = f"https://download.drobilla.net/{pkgname}-{pkgver}.tar.bz2"
sha256 = "26a37790890c9c1f838203b47f5b2320334fe92c02a4d26ebbe2669dbd769061"
options = ["!cross"]

def post_install(self):
    self.install_license("COPYING")
    self.rm(self.destdir / "usr/etc", recursive = True)

@subpackage("lilv-devel")
def _devel(self):
    return self.default_devel()

@subpackage("lilv-progs")
def _progs(self):
    return self.default_progs()
