pkgname = "union"
pkgver = "6.8.2"
pkgrel = 0
build_style = "cmake"
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
    "qt6-qtbase",
]
makedepends = [
    "breeze-devel",
    "cxx-rust-cssparser-devel",
    "kcolorscheme-devel",
    "kconfig-devel",
    "kcoreaddons-devel",
    "kguiaddons-devel",
    "kiconthemes-devel",
    "kirigami-devel",
    "qt6-qtbase-devel",
    "qt6-qtdeclarative-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "Style engine for KDE Plasma"
license = "LGPL-2.1-only OR LGPL-3.0-only"
url = "https://invent.kde.org/plasma/union"
source = f"$(KDE_SITE)/plasma/{pkgver}/union-{pkgver}.tar.xz"
sha256 = "a87b6cd9e04c7941d631cb0f243277aa84795738383e5153750a0ad1659e0353"


@subpackage("union-devel")
def _(self):
    return self.default_devel()
