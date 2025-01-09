pkgname = "syndication"
pkgver = "6.9.0"
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
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/syndication-{pkgver}.tar.xz"
sha256 = "642642c4c07fda0bc6314cb08602370b16c290f34463d2f44d44f0e5a6bfb1c2"
hardening = ["vis"]


def post_install(self):
    self.install_license("LICENSES/BSD-2-Clause.txt")


@subpackage("syndication-devel")
def _(self):
    return self.default_devel()
