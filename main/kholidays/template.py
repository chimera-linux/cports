pkgname = "kholidays"
pkgver = "6.31.0"
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
sha256 = "bdbbe8b1ae6ad6af2116e3ca2c986a317e00f215f58ad32000e2aae2b9d7d612"
hardening = ["vis"]


@subpackage("kholidays-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]

    return self.default_devel()
