pkgname = "phonon"
pkgver = "4.12.0"
pkgrel = 1
build_style = "cmake"
configure_args = ["-DPHONON_BUILD_QT5=OFF"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
    "pkgconf",
]
makedepends = [
    "libpulse-devel",
    "qt6-qt5compat-devel",
    "qt6-qtbase-devel",
    "qt6-qttools-devel",
]
pkgdesc = "KDE Multimedia backend"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.1-or-later"
url = "https://api.kde.org/phonon/html"
source = f"$(KDE_SITE)/phonon/{pkgver}/phonon-{pkgver}.tar.xz"
sha256 = "3287ffe0fbcc2d4aa1363f9e15747302d0b080090fe76e5f211d809ecb43f39a"
hardening = ["vis"]


@subpackage("phonon-devel")
def _(self):
    return self.default_devel()
