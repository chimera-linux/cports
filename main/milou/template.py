pkgname = "milou"
pkgver = "6.2.1"
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
    "ki18n-devel",
    "krunner-devel",
    "ksvg-devel",
    "kwindowsystem-devel",
    "libplasma-devel",
    "qt6-qtdeclarative-devel",
]
pkgdesc = "KDE Dedicated search application"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://api.kde.org/plasma/milou/html"
source = f"$(KDE_SITE)/plasma/{pkgver}/milou-{pkgver}.tar.xz"
sha256 = "715c10ac3d1ef4c6cd630aeb96a5ac21f912039a9b2dbe7f1abcf3793d0f8cd2"
hardening = ["vis"]
