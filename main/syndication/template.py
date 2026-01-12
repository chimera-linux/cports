pkgname = "syndication"
pkgver = "6.22.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "extra-cmake-modules", "ninja"]
makedepends = ["kcodecs-devel", "qt6-qttools-devel"]
pkgdesc = "KDE's RSS/Atom parser library"
license = "LGPL-2.0-or-later AND BSD-2-Clause"
url = "https://api.kde.org/frameworks/syndication/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/syndication-{pkgver}.tar.xz"
sha256 = "faf3a88e6711b06a35edf28c415fd665b5699a7cafee6fed2cb4997f318d8de0"
hardening = ["vis"]


def post_install(self):
    self.install_license("LICENSES/BSD-2-Clause.txt")


@subpackage("syndication-devel")
def _(self):
    return self.default_devel()
