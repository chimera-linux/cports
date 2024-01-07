pkgname = "jasper"
pkgver = "4.1.1"
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
source = f"https://github.com/jasper-software/{pkgname}/releases/download/version-{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "03ba86823f8798f3f60a5a34e36f3eff9e9cbd76175643a33d4aac7c0390240a"


def post_install(self):
    self.install_license("LICENSE.txt")


@subpackage("jasper-devel")
def _devel(self):
    self.depends += ["libjpeg-turbo-devel"]

    return self.default_devel()


@subpackage("jasper-progs")
def _progs(self):
    return self.default_progs()
