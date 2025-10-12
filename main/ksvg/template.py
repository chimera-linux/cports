pkgname = "ksvg"
pkgver = "6.19.0"
pkgrel = 0
build_style = "cmake"
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
hostmakedepends = ["cmake", "extra-cmake-modules", "ninja"]
makedepends = [
    "karchive-devel",
    "kcolorscheme-devel",
    "kconfig-devel",
    "kcoreaddons-devel",
    "kguiaddons-devel",
    "kirigami-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qtsvg-devel",
    "qt6-qttools-devel",
]
pkgdesc = "KDE Components for handling SVGs"
license = "LGPL-2.0-or-later AND GPL-2.0-or-later"
url = "https://invent.kde.org/frameworks/ksvg"
source = (
    f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/ksvg-{pkgver}.tar.xz"
)
sha256 = "92a2cbc4604a3ea86d9b8ad921adff93646156017bc8fa5c75958ef324b5e9ef"
hardening = ["vis"]


@subpackage("ksvg-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]
    return self.default_devel()
