pkgname = "kdecoration"
pkgver = "6.7.1"
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
sha256 = "3a5d8f57bab452eabd1aadc45088b95a669a951626c7e601f6a0ef36030684bf"
hardening = ["vis"]


@subpackage("kdecoration-devel")
def _(self):
    return self.default_devel()
