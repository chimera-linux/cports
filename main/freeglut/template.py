pkgname = "freeglut"
pkgver = "3.2.2"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["libxxf86vm-devel", "libxi-devel", "mesa-devel", "glu-devel"]
pkgdesc = "Open source implementation of the OpenGL Utility Toolkit library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "http://freeglut.sourceforge.net"
source = f"$(SOURCEFORGE_SITE)/{pkgname}/{pkgname}-{pkgver}.tar.gz"
sha256 = "c5944a082df0bba96b5756dddb1f75d0cd72ce27b5395c6c1dde85c2ff297a50"
tool_flags = {"CFLAGS": ["-fcommon"]}
# no tests
options = ["!check"]

def post_install(self):
    self.install_license("COPYING")

@subpackage("freeglut-devel")
def _devel(self):
    self.depends += makedepends
    return self.default_devel()
