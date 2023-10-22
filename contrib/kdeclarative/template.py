pkgname = "kdeclarative"
pkgver = "6.2.0"
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
sha256 = "a85c3f1599d229f052ee3786e9041ace5510c99844c8efc7bfc9ddaed1936d84"
hardening = ["vis", "cfi"]


@subpackage("kdeclarative-devel")
def _devel(self):
    self.depends += ["kconfig-devel"]

    return self.default_devel()
