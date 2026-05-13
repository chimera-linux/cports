pkgname = "kdecoration"
pkgver = "6.6.5"
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
sha256 = "06e8ed04b8f3cdcd3057a9e2d23291ef41a3976f96fc8cf917479218871aa9fd"
hardening = ["vis"]


@subpackage("kdecoration-devel")
def _(self):
    return self.default_devel()
