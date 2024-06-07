pkgname = "ktnef"
pkgver = "24.05.0"
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
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.0-or-later"
url = "https://api.kde.org/kdepim/ktnef/html"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/ktnef-{pkgver}.tar.xz"
sha256 = "86d845160c2a59bef191f0ac35e11630e921239efc6c6fef98ea540f74ee07aa"


@subpackage("ktnef-devel")
def _devel(self):
    self.depends += ["kcalendarcore-devel"]
    return self.default_devel()
