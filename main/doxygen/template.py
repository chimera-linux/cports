pkgname = "doxygen"
pkgver = "1.9.3"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "perl", "python", "flex", "bison"]
checkdepends = ["libxml2-progs"]
pkgdesc = "Source code documentation generator tool"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only"
url = "https://doxygen.nl"
source = f"{url}/files/{pkgname}-{pkgver}.src.tar.gz"
sha256 = "f352dbc3221af7012b7b00935f2dfdc9fb67a97d43287d2f6c81c50449d254e0"

def post_extract(self):
    # needs texlive stuff
    self.rm("testing/012_cite.dox")

def post_install(self):
    self.install_man("doc/doxygen.1")
