pkgname = "freeglut"
pkgver = "3.2.1"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["libxxf86vm-devel", "libxi-devel", "mesa-devel", "glu-devel"]
pkgdesc = "Open source implementation of the OpenGL Utility Toolkit library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "http://freeglut.sourceforge.net"
source = f"$(SOURCEFORGE_SITE)/{pkgname}/{pkgname}-{pkgver}.tar.gz"
sha256 = "d4000e02102acaf259998c870e25214739d1f16f67f99cb35e4f46841399da68"
tool_flags = {"CFLAGS": ["-fcommon"]}
# no tests
options = ["!check"]

def post_install(self):
    self.install_license("COPYING")

@subpackage("freeglut-devel")
def _devel(self):
    self.depends += makedepends
    return self.default_devel(man = True)
