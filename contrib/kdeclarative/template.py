pkgname = "kdeclarative"
pkgver = "6.5.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
]
makedepends = [
    "kconfig-devel",
    "kglobalaccel-devel",
    "kguiaddons-devel",
    "ki18n-devel",
    "kwidgetsaddons-devel",
    "qt6-qtdeclarative-devel",
]
pkgdesc = "KDE Integration of QML and KDE work spaces"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.1-or-later"
url = "https://api.kde.org/frameworks/kdeclarative/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[:pkgver.rfind('.')]}/kdeclarative-{pkgver}.tar.xz"
sha256 = "b3c4152c972e3d53645f1c88757a78ce5b66fbf4ecb76e4d69df78d2ab38cf83"
hardening = ["vis"]


@subpackage("kdeclarative-devel")
def _devel(self):
    self.depends += ["kconfig-devel", "qt6-qtdeclarative-devel"]

    return self.default_devel()
