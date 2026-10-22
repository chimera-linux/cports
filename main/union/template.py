pkgname = "union"
pkgver = "6.8.1"
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
sha256 = "abea413c79fe9a52337a9b8a50ee8fb29be7ed38bd764eb7555d724e99b39f00"


@subpackage("union-devel")
def _(self):
    return self.default_devel()
