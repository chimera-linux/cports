pkgname = "doxygen"
pkgver = "1.14.0"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DCMAKE_BUILD_TYPE=Release"]
hostmakedepends = ["cmake", "ninja", "perl", "python", "flex", "bison"]
checkdepends = ["libxml2-progs"]
pkgdesc = "Source code documentation generator tool"
license = "GPL-2.0-only"
url = "https://doxygen.nl"
source = f"{url}/files/doxygen-{pkgver}.src.tar.gz"
sha256 = "d4536d11ab13037327d8d026b75f5a86b7ccb2093e2f546235faf61fd86e6b5d"
hardening = ["vis", "cfi"]


def post_extract(self):
    # needs texlive stuff
    self.rm("testing/012_cite.dox")
    # xmllint produces different outputs on semantically identical input
    self.rm("testing/009_bug.cpp")


def post_install(self):
    self.install_man("doc/doxygen.1")
