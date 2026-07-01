pkgname = "qqc2-breeze-style"
pkgver = "6.7.2"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
    "pkgconf",
]
makedepends = [
    "kcolorscheme-devel",
    "kconfig-devel",
    "kcoreaddons-devel",
    "kguiaddons-devel",
    "kiconthemes-devel",
    "kirigami-devel",
    "kquickcharts-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qttools-devel",
]
pkgdesc = "Breeze inspired QQC2 style"
license = "LGPL-2.0-or-later"
url = "https://invent.kde.org/plasma/qqc2-breeze-style"
source = f"$(KDE_SITE)/plasma/{pkgver}/qqc2-breeze-style-{pkgver}.tar.xz"
sha256 = "94e1dad9b110c43d48d8bea7c12e7fa2754e56d1a05a7bb249a03035e77f5b49"
hardening = ["vis"]


@subpackage("qqc2-breeze-style-devel")
def _(self):
    return self.default_devel()
