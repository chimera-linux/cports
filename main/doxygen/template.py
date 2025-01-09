pkgname = "doxygen"
pkgver = "1.13.1"
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
sha256 = "b593a17e9f7dd00c253d5bb18f05b84632136e89753b87fe366c858ea63f6e62"
hardening = ["vis", "cfi"]


def post_extract(self):
    # needs texlive stuff
    self.rm("testing/012_cite.dox")


def post_install(self):
    self.install_man("doc/doxygen.1")
