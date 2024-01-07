pkgname = "doxygen"
pkgver = "1.10.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "perl", "python", "flex", "bison"]
checkdepends = ["libxml2-progs"]
pkgdesc = "Source code documentation generator tool"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only"
url = "https://doxygen.nl"
source = f"{url}/files/{pkgname}-{pkgver}.src.tar.gz"
sha256 = "dd7c556b4d96ca5e682534bc1f1a78a5cfabce0c425b14c1b8549802686a4442"
hardening = ["vis", "cfi"]


def post_extract(self):
    # needs texlive stuff
    self.rm("testing/012_cite.dox")


def post_install(self):
    self.install_man("doc/doxygen.1")
