pkgname = "kholidays"
pkgver = "6.30.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "bison",
    "cmake",
    "extra-cmake-modules",
    "flex",
    "ninja",
]
makedepends = [
    "qt6-qtdeclarative-devel",
    "qt6-qttools-devel",
]
pkgdesc = "KDE library for holiday dates"
license = "LGPL-2.0-or-later"
url = "https://community.kde.org/Frameworks"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kholidays-{pkgver}.tar.xz"
sha256 = "02bfbc33296fe86b364491f6d5cad9d83360bb4fdd2923386a325b309eac0b9b"
hardening = ["vis"]


@subpackage("kholidays-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]

    return self.default_devel()
