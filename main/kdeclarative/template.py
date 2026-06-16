pkgname = "kdeclarative"
pkgver = "6.27.0"
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
sha256 = "b14e81143aed25ee62413f9c2b3742c558f5b6a1da6c5b92ca9a95bb6341e964"
hardening = ["vis"]


@subpackage("kdeclarative-devel")
def _(self):
    self.depends += ["kconfig-devel", "qt6-qtdeclarative-devel"]

    return self.default_devel()
