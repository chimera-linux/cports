pkgname = "kholidays"
pkgver = "6.15.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
]
makedepends = [
    "qt6-qtdeclarative-devel",
    "qt6-qttools-devel",
]
pkgdesc = "KDE library for holiday dates"
license = "LGPL-2.0-or-later"
url = "https://api.kde.org/frameworks/kholidays/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kholidays-{pkgver}.tar.xz"
sha256 = "396860b9d63d3bb8f0cb0c433e0bb3cf7721394842f3fb8389c83e07ba0ae695"
hardening = ["vis"]


@subpackage("kholidays-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]

    return self.default_devel()
