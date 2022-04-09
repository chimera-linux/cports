pkgname = "jasper"
pkgver = "3.0.3"
pkgrel = 0
build_style = "cmake"
make_dir = "jbuild" # build is taken
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["libjpeg-turbo-devel"]
pkgdesc = "Reference implementation of the JPEG-2000 codec"
maintainer = "q66 <q66@chimera-linux.org>"
license = "JasPer-2.0"
url = "https://ece.engr.uvic.ca/~frodo/jasper"
source = f"https://github.com/jasper-software/{pkgname}/releases/download/version-{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "7c2ae6e10f0e4988277aba9d6d15cbf4f73576e9372c1749366e565b68c76eae"

def post_install(self):
    self.install_license("LICENSE.txt")

@subpackage("jasper-devel")
def _devel(self):
    self.depends += ["libjpeg-turbo-devel"]

    return self.default_devel()

@subpackage("jasper-progs")
def _progs(self):
    return self.default_progs()
