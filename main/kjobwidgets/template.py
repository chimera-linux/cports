pkgname = "kjobwidgets"
pkgver = "6.11.0"
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
    "qt6-qtbase-private-devel",  # qtx11extras_p.h
    "qt6-qttools-devel",
]
pkgdesc = "KDE Widgets for showing progress of asynchronous jobs"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.1-only AND (LGPL-2.1-only OR LGPL-3.0-only)"
url = "https://api.kde.org/frameworks/kjobwidgets/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kjobwidgets-{pkgver}.tar.xz"
sha256 = "2bb342e554f8ecf84d7218a6567628dcc73c1b914d0c5aad1c8bf7753986ddd7"
hardening = ["vis"]


@subpackage("kjobwidgets-devel")
def _(self):
    return self.default_devel()
