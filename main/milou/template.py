pkgname = "milou"
pkgver = "6.4.0"
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
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://invent.kde.org/plasma/milou"
source = f"$(KDE_SITE)/plasma/{pkgver}/milou-{pkgver}.tar.xz"
sha256 = "ed258ac78b47d8eee8171388abc12dc73baf3fe8242bc119a6a31431d7db3f30"
hardening = ["vis"]
