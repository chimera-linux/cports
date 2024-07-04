pkgname = "ktnef"
pkgver = "24.05.2"
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
sha256 = "08154a15224f63c8a313596ddd5e702fd48bcc43350730698cc66a0ba31b21ec"


@subpackage("ktnef-devel")
def _devel(self):
    self.depends += ["kcalendarcore-devel"]
    return self.default_devel()
