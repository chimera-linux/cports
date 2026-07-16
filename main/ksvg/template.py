pkgname = "ksvg"
pkgver = "6.28.0"
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
sha256 = "d580e6038ab3fb8a8755c953abd27a55894c2ae05e72cdef9bca1cf4e265a325"
hardening = ["vis"]
# expects installed imagesets
options = ["!check"]


@subpackage("ksvg-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]
    return self.default_devel()
