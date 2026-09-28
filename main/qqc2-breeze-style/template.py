pkgname = "qqc2-breeze-style"
pkgver = "6.7.5"
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
sha256 = "788f0698c904112cc33bf6f8fb446b2e4fd7231d38c0955cbc3baa50d375d1ee"
hardening = ["vis"]


@subpackage("qqc2-breeze-style-devel")
def _(self):
    return self.default_devel()
