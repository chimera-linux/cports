pkgname = "union"
pkgver = "6.8.0"
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
sha256 = "d7340ffe4e269c6ee676acc6c93b928932b06ee2654ae3e7b904b699fb46a46c"


@subpackage("union-devel")
def _(self):
    return self.default_devel()
