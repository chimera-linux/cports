pkgname = "kcompletion"
pkgver = "6.28.0"
pkgrel = 0
build_style = "cmake"
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
]
makedepends = [
    "kcodecs-devel",
    "kconfig-devel",
    "kwidgetsaddons-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qttools-devel",
]
pkgdesc = "KDE Powerful completion framework"
license = "LGPL-2.1-or-later"
url = "https://api.kde.org/frameworks/kcompletion/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kcompletion-{pkgver}.tar.xz"
sha256 = "8aa9cbc36139adfa8e3b2c744cc94714afe154d21cef8a3a2d5f4d311be7cc3c"
hardening = ["vis"]


@subpackage("kcompletion-devel")
def _(self):
    return self.default_devel()
