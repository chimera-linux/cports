pkgname = "kdecoration"
pkgver = "6.7.2"
pkgrel = 0
build_style = "cmake"
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
]
makedepends = [
    "ki18n-devel",
    "qt6-qtbase-devel",
]
pkgdesc = "KDE Plugin based library to create window decorations"
license = "LGPL-2.1-only OR LGPL-3.0-only"
url = "https://api.kde.org/plasma/kdecoration/html"
source = f"$(KDE_SITE)/plasma/{pkgver}/kdecoration-{pkgver}.tar.xz"
sha256 = "c82e28e59d2cc2e31ae38e3bc48579528214ba3da2d13a2b71a65bdc0dc47771"
hardening = ["vis"]


@subpackage("kdecoration-devel")
def _(self):
    return self.default_devel()
