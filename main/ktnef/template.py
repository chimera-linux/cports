pkgname = "ktnef"
pkgver = "26.08.1"
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
sha256 = "f044833403ac6d9352287ccaed35af4eea07a95b9d89dfb740b01061e5af48a1"


@subpackage("ktnef-devel")
def _(self):
    self.depends += ["kcalendarcore-devel"]
    return self.default_devel()
