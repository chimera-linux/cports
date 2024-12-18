pkgname = "ktnef"
pkgver = "24.12.0"
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
sha256 = "0a7677d2acf7e25f5199e1acd9a3422370eff9a309ddd27740657768cbdd0660"


@subpackage("ktnef-devel")
def _(self):
    self.depends += ["kcalendarcore-devel"]
    return self.default_devel()
