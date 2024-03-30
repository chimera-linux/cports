pkgname = "neofetch"
pkgver = "7.1.0"
pkgrel = 1
build_style = "makefile"
depends = ["bash"]
pkgdesc = "Simple system information script"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/dylanaraps/neofetch"
source = f"{url}/archive/{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "58a95e6b714e41efc804eca389a223309169b2def35e57fa934482a6b47c27e7"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.md")
