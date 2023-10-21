pkgname = "syndication"
pkgver = "6.2.0"
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
sha256 = "50ec3843a08ec7b185352c94b89bc2d2720ceaf17eb961a4c3da55f93d05af3c"
# FIXME: cfi breaks 2/3 tests
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_license("LICENSES/BSD-2-Clause.txt")


@subpackage("syndication-devel")
def _devel(self):
    return self.default_devel()
