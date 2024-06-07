pkgname = "kholidays"
pkgver = "6.3.0"
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
sha256 = "9f99e118c73da1d53805cb38ee876115d75ad5eb5fb108a38e6ae880e7cfac5e"
hardening = ["vis", "!cfi"]


@subpackage("kholidays-devel")
def _devel(self):
    self.depends += ["qt6-qtbase-devel"]

    return self.default_devel()
