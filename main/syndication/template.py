pkgname = "syndication"
pkgver = "6.31.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "extra-cmake-modules", "ninja"]
makedepends = ["kcodecs-devel", "qt6-qttools-devel"]
pkgdesc = "KDE's RSS/Atom parser library"
license = "LGPL-2.0-or-later AND BSD-2-Clause"
url = "https://community.kde.org/Frameworks"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/syndication-{pkgver}.tar.xz"
sha256 = "7cd3ac299ff01736b7a9a1a2eb3700561810267a2e3af50935c3f3cce9635077"
hardening = ["vis"]


def post_install(self):
    self.install_license("LICENSES/BSD-2-Clause.txt")


@subpackage("syndication-devel")
def _(self):
    return self.default_devel()
