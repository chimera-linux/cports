pkgname = "doxygen"
pkgver = "1.13.0"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DCMAKE_BUILD_TYPE=Release"]
hostmakedepends = ["cmake", "ninja", "perl", "python", "flex", "bison"]
checkdepends = ["libxml2-progs"]
pkgdesc = "Source code documentation generator tool"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only"
url = "https://doxygen.nl"
source = f"{url}/files/doxygen-{pkgver}.src.tar.gz"
sha256 = "99434f8130f68be4a4a817e540620aedf95c617c68cc73434de04207abaaae46"
hardening = ["vis", "cfi"]


def post_extract(self):
    # needs texlive stuff
    self.rm("testing/012_cite.dox")


def post_install(self):
    self.install_man("doc/doxygen.1")
