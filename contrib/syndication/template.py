pkgname = "syndication"
pkgver = "6.4.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
]
makedepends = [
    "kcodecs-devel",
    "qt6-qtbase-devel",
]
pkgdesc = "KDE's RSS/Atom parser library"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.0-or-later AND BSD-2-Clause"
url = "https://api.kde.org/frameworks/syndication/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[:pkgver.rfind('.')]}/syndication-{pkgver}.tar.xz"
sha256 = "d5637eaf255c4d3e110765d2ed5aba06c994560801e4e6c4b0698acc53954dcb"
# CFI: breaks 2/3 tests
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_license("LICENSES/BSD-2-Clause.txt")


@subpackage("syndication-devel")
def _devel(self):
    return self.default_devel()
