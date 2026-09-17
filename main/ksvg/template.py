pkgname = "ksvg"
pkgver = "6.30.0"
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
sha256 = "7b7aba4e9baa88bfb303977e139e8a105b5cd243443029ee773954307b51eb91"
hardening = ["vis"]
# expects installed imagesets
options = ["!check"]


@subpackage("ksvg-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]
    return self.default_devel()
