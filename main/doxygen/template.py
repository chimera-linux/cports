pkgname = "doxygen"
pkgver = "1.9.5"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "perl", "python", "flex", "bison"]
checkdepends = ["libxml2-progs"]
pkgdesc = "Source code documentation generator tool"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only"
url = "https://doxygen.nl"
source = f"{url}/files/{pkgname}-{pkgver}.src.tar.gz"
sha256 = "55b454b35d998229a96f3d5485d57a0a517ce2b78d025efb79d57b5a2e4b2eec"

def post_extract(self):
    # needs texlive stuff
    self.rm("testing/012_cite.dox")

def post_install(self):
    self.install_man("doc/doxygen.1")
