pkgname = "qqc2-breeze-style"
pkgver = "6.4.2"
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
sha256 = "36e05b1b227b5b659b8b0b886dc34dfec21b09925bef4ec3e71ef28325c6ec89"
hardening = ["vis"]


@subpackage("qqc2-breeze-style-devel")
def _(self):
    return self.default_devel()
