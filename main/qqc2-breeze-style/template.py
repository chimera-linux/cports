pkgname = "qqc2-breeze-style"
pkgver = "6.5.1"
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
sha256 = "8ca3a0996a4dce06c9a61998afe140201f60c0119a037aebbc07fc3d7a28d0a0"
hardening = ["vis"]


@subpackage("qqc2-breeze-style-devel")
def _(self):
    return self.default_devel()
