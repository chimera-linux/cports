pkgname = "jasper"
pkgver = "4.2.4"
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
sha256 = "6a597613d8d84c500b5b83bf0eec06cd3707c23d19957f70354ac2394c9914e7"


def post_install(self):
    self.install_license("LICENSE.txt")


@subpackage("jasper-devel")
def _devel(self):
    self.depends += ["libjpeg-turbo-devel"]

    return self.default_devel()


@subpackage("jasper-progs")
def _progs(self):
    return self.default_progs()
