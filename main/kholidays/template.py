pkgname = "kholidays"
pkgver = "6.8.0"
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
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.0-or-later"
url = "https://api.kde.org/frameworks/kholidays/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[:pkgver.rfind('.')]}/kholidays-{pkgver}.tar.xz"
sha256 = "162b8ade42de80415380f6476a285fbfab5bb270f35b0d7d13baa1c34a5fb164"
hardening = ["vis"]


@subpackage("kholidays-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]

    return self.default_devel()
