pkgname = "ktnef"
pkgver = "26.08.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "kcalendarcore-devel",
    "kcalutils-devel",
    "kcontacts-devel",
    "ki18n-devel",
    "qt6-qtbase-devel",
]
pkgdesc = "KDE library for TNEF data"
license = "LGPL-2.0-or-later"
url = "https://community.kde.org/KDE_PIM"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/ktnef-{pkgver}.tar.xz"
sha256 = "b7f6be661f45695596f88e964b05ef4db5d8f878df1a9c852fb8dd65ecb4e25e"


@subpackage("ktnef-devel")
def _(self):
    self.depends += ["kcalendarcore-devel"]
    return self.default_devel()
