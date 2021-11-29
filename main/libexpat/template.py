pkgname = "libexpat"
pkgver = "2.4.1"
pkgrel = 0
build_style = "gnu_configure"
make_check_args = ["-j1"]
hostmakedepends = ["pkgconf"]
pkgdesc = "XML parser library written in C"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://libexpat.github.io"
source = f"https://github.com/{pkgname}/{pkgname}/releases/download/R_{pkgver.replace('.', '_')}/expat-{pkgver}.tar.xz"
sha256 = "cf032d0dba9b928636548e32b327a2d66b1aab63c4f4a13dd132c2d1d2f2fb6a"

def post_install(self):
    self.install_license("COPYING")

@subpackage("libexpat-static")
def _static(self):
    return self.default_static()

@subpackage("libexpat-devel")
def _devel(self):
    return self.default_devel(man = True)

@subpackage("xmlwf")
def _xmlwf(self):
    self.pkgdesc = f"{pkgdesc} (xmlwf utility)"
    return self.default_progs(man = True)
