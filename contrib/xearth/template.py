pkgname = "xearth"
pkgver = "1.1"
pkgrel = 0
build_style = "makefile"
make_build_args = ["-f", "Makefile.DIST"]
makedepends = ["libx11-devel", "libxt-devel"]
pkgdesc = "Set the X11 root window to an image of the Earth"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:xearth"
url = "https://xearth.org"
source = f"https://xearth.org/xearth-{pkgver}.tar.gz"
sha256 = "bcb1407cc35b3f6dd3606b2c6072273b6a912cbd9ed1ae22fb2d26694541309c"
tool_flags = {"CFLAGS": ["-Wno-deprecated-non-prototype"]}
# no tests
options = ["!check"]


def install(self):
    self.install_bin("xearth")
    self.install_man("xearth.man", name="xearth", cat=1)
    self.install_license("README")
