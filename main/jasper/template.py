pkgname = "jasper"
pkgver = "4.1.2"
pkgrel = 0
build_style = "cmake"
configure_args = [
    # checks for subdir of source tree, so srcdir/jbuild is 'in-source'
    "-DALLOW_IN_SOURCE_BUILD=ON",
]
make_dir = "jbuild"  # build is taken
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["libjpeg-turbo-devel"]
pkgdesc = "Reference implementation of the JPEG-2000 codec"
maintainer = "q66 <q66@chimera-linux.org>"
license = "JasPer-2.0"
url = "https://ece.engr.uvic.ca/~frodo/jasper"
source = f"https://github.com/jasper-software/jasper/releases/download/version-{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "22392e439b87c79aaf8689ec79a286a7147e811c4bee34edf3d0b239798d672b"


def post_install(self):
    self.install_license("LICENSE.txt")


@subpackage("jasper-devel")
def _devel(self):
    self.depends += ["libjpeg-turbo-devel"]

    return self.default_devel()


@subpackage("jasper-progs")
def _progs(self):
    return self.default_progs()
