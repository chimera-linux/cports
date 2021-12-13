pkgname = "doxygen"
pkgver = "1.9.2"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "perl", "python", "flex", "bison"]
checkdepends = ["libxml2-progs"]
pkgdesc = "Source code documentation generator tool"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only"
url = "https://doxygen.nl"
source = f"{url}/files/{pkgname}-{pkgver}.src.tar.gz"
sha256 = "060f254bcef48673cc7ccf542736b7455b67c110b30fdaa33512a5b09bbecee5"

def post_extract(self):
    # needs texlive stuff
    self.rm("testing/012_cite.dox")

def post_install(self):
    self.install_man("doc/doxygen.1")
