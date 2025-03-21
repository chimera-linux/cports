pkgname = "kcoreaddons"
pkgver = "6.12.0"
pkgrel = 0
build_style = "cmake"
# flaky
make_check_args = ["-E", "knetworkmountstestnoconfig"]
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
]
makedepends = [
    "qt6-qtdeclarative-devel",
    "qt6-qttools-devel",
]
pkgdesc = "Qt6 addon library with a collection of non-GUI utilities"
license = "LGPL-2.0-or-later AND (LGPL-2.1-only OR LGPL-3.0-only)"
url = "https://api.kde.org/frameworks/kcoreaddons/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kcoreaddons-{pkgver}.tar.xz"
sha256 = "7b37e8d4e185bcdd8bfd166c739f7adbcb0730cdf140d64a308f7b96b1845736"
hardening = ["vis"]


@subpackage("kcoreaddons-devel")
def _(self):
    return self.default_devel()
