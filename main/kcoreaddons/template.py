pkgname = "kcoreaddons"
pkgver = "6.13.0"
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
sha256 = "a110bc3303c541fbac3e2d3aa93c2eb25413055de24634a69034210f6dfddbdb"
hardening = ["vis"]


@subpackage("kcoreaddons-devel")
def _(self):
    return self.default_devel()
