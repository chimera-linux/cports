pkgname = "qt6ct"
pkgver = "0.9"
pkgrel = 13
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "qt6-qttools", "qt6-qtbase"]
makedepends = [
    "qt6-qtbase-private-devel",  # qgenericunixthemes_p.h etc
    "qt6-qttools-devel",
]
depends = ["qt6-qtsvg"]
pkgdesc = "Qt6 configuration tool"
license = "BSD-2-Clause"
url = "https://github.com/trialuser02/qt6ct"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "aa49c4fb51a82dd6947cd9c8dee9b3a1fdd4fbbc9f3c8c5c2d33fa1de9e8826e"


def post_install(self):
    self.install_license("COPYING")
