pkgname = "jasper"
pkgver = "4.2.5"
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
license = "JasPer-2.0"
url = "https://ece.engr.uvic.ca/~frodo/jasper"
source = f"https://github.com/jasper-software/jasper/releases/download/version-{pkgver}/jasper-{pkgver}.tar.gz"
sha256 = "6e49075b47204a9879600f85628a248cdb19abc1bb74d0b7a2177bcdb87c95eb"


def post_install(self):
    self.install_license("LICENSE.txt")


@subpackage("jasper-devel")
def _(self):
    self.depends += ["libjpeg-turbo-devel"]

    return self.default_devel()


@subpackage("jasper-progs")
def _(self):
    return self.default_progs()
