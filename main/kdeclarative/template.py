pkgname = "kdeclarative"
pkgver = "6.30.0"
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
url = "https://community.kde.org/Frameworks"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kdeclarative-{pkgver}.tar.xz"
sha256 = "7ec3583a2cf2cd7143e39936ffb39e22d20563f4c87a8462e0e9d12c59ea89a6"
hardening = ["vis"]


@subpackage("kdeclarative-devel")
def _(self):
    self.depends += ["kconfig-devel", "qt6-qtdeclarative-devel"]

    return self.default_devel()
