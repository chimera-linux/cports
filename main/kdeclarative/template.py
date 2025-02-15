pkgname = "kdeclarative"
pkgver = "6.11.0"
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
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kdeclarative-{pkgver}.tar.xz"
sha256 = "6ae811367bcbc8190f8a5d2ef39a8e6c72871c41ec26e2a4b0c38324a3e8596b"
hardening = ["vis"]


@subpackage("kdeclarative-devel")
def _(self):
    self.depends += ["kconfig-devel", "qt6-qtdeclarative-devel"]

    return self.default_devel()
