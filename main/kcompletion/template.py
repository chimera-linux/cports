pkgname = "kcompletion"
pkgver = "6.31.0"
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
url = "https://community.kde.org/Frameworks"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kcompletion-{pkgver}.tar.xz"
sha256 = "b9b0023059c09fadfd9aa5d6cf40b3fb0a72d9b45e73b2146c29c20dfab35689"
hardening = ["vis"]


@subpackage("kcompletion-devel")
def _(self):
    return self.default_devel()
