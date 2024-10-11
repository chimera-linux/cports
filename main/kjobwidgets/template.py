pkgname = "kjobwidgets"
pkgver = "6.7.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
]
makedepends = [
    "kcoreaddons-devel",
    "knotifications-devel",
    "kwidgetsaddons-devel",
    "qt6-qtbase-devel",
    "qt6-qttools-devel",
]
pkgdesc = "KDE Widgets for showing progress of asynchronous jobs"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.1-only AND (LGPL-2.1-only OR LGPL-3.0-only)"
url = "https://api.kde.org/frameworks/kjobwidgets/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[:pkgver.rfind('.')]}/kjobwidgets-{pkgver}.tar.xz"
sha256 = "16d7e7ab54235d6fa1eb213d3d637182e22fcbdbcb7b4b14032430a02a2f888a"
hardening = ["vis"]


@subpackage("kjobwidgets-devel")
def _(self):
    return self.default_devel()
