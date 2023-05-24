pkgname = "freeglut"
pkgver = "3.4.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["libxxf86vm-devel", "libxi-devel", "mesa-devel", "glu-devel"]
pkgdesc = "Open source implementation of the OpenGL Utility Toolkit library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "http://freeglut.sourceforge.net"
source = f"$(SOURCEFORGE_SITE)/{pkgname}/{pkgname}-{pkgver}.tar.gz"
sha256 = "3c0bcb915d9b180a97edaebd011b7a1de54583a838644dcd42bb0ea0c6f3eaec"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("freeglut-devel")
def _devel(self):
    self.depends += makedepends
    return self.default_devel()
