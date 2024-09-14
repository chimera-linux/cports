pkgname = "kjobwidgets"
pkgver = "6.6.0"
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
sha256 = "3c8eccd89d4118b6ecd619106f93a9b156df5899465b820d4b65d969813db515"
hardening = ["vis"]


@subpackage("kjobwidgets-devel")
def _(self):
    return self.default_devel()
