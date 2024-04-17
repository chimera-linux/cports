pkgname = "qt6ct"
pkgver = "0.9"
pkgrel = 2
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "qt6-qttools", "qt6-qtbase"]
makedepends = ["qt6-qtbase-devel", "qt6-qttools-devel"]
depends = ["qt6-qtsvg"]
pkgdesc = "Qt6 configuration tool"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://github.com/trialuser02/qt6ct"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "aa49c4fb51a82dd6947cd9c8dee9b3a1fdd4fbbc9f3c8c5c2d33fa1de9e8826e"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("COPYING")
