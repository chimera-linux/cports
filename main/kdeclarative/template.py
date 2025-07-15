pkgname = "kdeclarative"
pkgver = "6.16.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "extra-cmake-modules", "gettext", "ninja"]
makedepends = [
    "kconfig-devel",
    "kglobalaccel-devel",
    "kguiaddons-devel",
    "ki18n-devel",
    "kwidgetsaddons-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qttools-devel",
]
pkgdesc = "KDE Integration of QML and KDE work spaces"
license = "LGPL-2.1-or-later"
url = "https://api.kde.org/frameworks/kdeclarative/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kdeclarative-{pkgver}.tar.xz"
sha256 = "c58df7a1f501286f96d0cf0b396598ede16eb3cadbc8a05d35236ce4df31c80e"
hardening = ["vis"]


@subpackage("kdeclarative-devel")
def _(self):
    self.depends += ["kconfig-devel", "qt6-qtdeclarative-devel"]

    return self.default_devel()
