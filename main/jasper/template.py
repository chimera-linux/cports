pkgname = "jasper"
pkgver = "4.1.0"
pkgrel = 0
build_style = "cmake"
make_dir = "jbuild"  # build is taken
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["libjpeg-turbo-devel"]
pkgdesc = "Reference implementation of the JPEG-2000 codec"
maintainer = "q66 <q66@chimera-linux.org>"
license = "JasPer-2.0"
url = "https://ece.engr.uvic.ca/~frodo/jasper"
source = f"https://github.com/jasper-software/{pkgname}/releases/download/version-{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "ffe1543d87f7ffc5039d2415afd48c314a7cc0b0c750b4982cd881d6ed4b5743"


def post_install(self):
    self.install_license("LICENSE.txt")


@subpackage("jasper-devel")
def _devel(self):
    self.depends += ["libjpeg-turbo-devel"]

    return self.default_devel()


@subpackage("jasper-progs")
def _progs(self):
    return self.default_progs()
