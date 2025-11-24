pkgname = "syndication"
pkgver = "6.20.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "extra-cmake-modules", "ninja"]
makedepends = ["kcodecs-devel", "qt6-qttools-devel"]
pkgdesc = "KDE's RSS/Atom parser library"
license = "LGPL-2.0-or-later AND BSD-2-Clause"
url = "https://api.kde.org/frameworks/syndication/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/syndication-{pkgver}.tar.xz"
sha256 = "e2b79ea958a8edfd4c9c0790925cc43d1f4031ec65ee545a60591008be159242"
hardening = ["vis"]


def post_install(self):
    self.install_license("LICENSES/BSD-2-Clause.txt")


@subpackage("syndication-devel")
def _(self):
    return self.default_devel()
