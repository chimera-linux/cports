pkgname = "ktnef"
pkgver = "26.08.3"
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
sha256 = "badb933874840b1fc2566297be4182b00f1ea2ecf0385d800a8537f7cd209fa1"


@subpackage("ktnef-devel")
def _(self):
    self.depends += ["kcalendarcore-devel"]
    return self.default_devel()
