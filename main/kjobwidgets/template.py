pkgname = "kjobwidgets"
pkgver = "6.9.0"
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
sha256 = "81867978a3add5c2539e6ac4cfd1711ae44ceb50f4654f598c5dd0ab05553716"
hardening = ["vis"]


@subpackage("kjobwidgets-devel")
def _(self):
    return self.default_devel()
