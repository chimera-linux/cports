pkgname = "qt6ct"
pkgver = "0.8"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "qt6-qttools", "qt6-qtbase"]
makedepends = ["qt6-qtbase-devel", "qt6-qttools-devel"]
depends = ["qt6-qtsvg"]
pkgdesc = "Qt6 configuration tool"
license = "BSD-2-Clause"
url = "https://github.com/trialuser02/qt6ct"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "ca3706770cbdbce769ee4393de9f7469be043810fe40283690612f5f6552018a"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("COPYING")
