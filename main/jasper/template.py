pkgname = "jasper"
pkgver = "3.0.6"
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
sha256 = "169be004d91f6940c649a4f854ada2755d4f35f62b0555ce9e1219c778cffc09"

def post_install(self):
    self.install_license("LICENSE.txt")

@subpackage("jasper-devel")
def _devel(self):
    self.depends += ["libjpeg-turbo-devel"]

    return self.default_devel()

@subpackage("jasper-progs")
def _progs(self):
    return self.default_progs()
