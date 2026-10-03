pkgname = "qqc2-breeze-style"
pkgver = "6.7.91"
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
source = (
    f"$(KDE_UNSTABLE_SITE)/plasma/{pkgver}/qqc2-breeze-style-{pkgver}.tar.xz"
)
sha256 = "15f1306b9edb83002af948d03baac68cdb4d5a3239bb7447dc148c5f885b24d8"
hardening = ["vis"]


@subpackage("qqc2-breeze-style-devel")
def _(self):
    return self.default_devel()
