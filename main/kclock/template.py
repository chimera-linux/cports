pkgname = "kclock"
pkgver = "25.08.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "kconfig-devel",
    "kcoreaddons-devel",
    "kcrash-devel",
    "kdbusaddons-devel",
    "ki18n-devel",
    "kio-devel",
    "kirigami-addons-devel",
    "kirigami-devel",
    "knotifications-devel",
    "kstatusnotifieritem-devel",
    "ksvg-devel",
    "libplasma-devel",
    "qt6-qtmultimedia-devel",
    "qt6-qtsvg-devel",
]
depends = ["kirigami-addons"]
pkgdesc = "KDE clock"
license = "GPL-3.0-or-later AND LGPL-2.1-or-later"
url = "https://apps.kde.org/kclock"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kclock-{pkgver}.tar.xz"
sha256 = "b0fe8c3a4c423c5ca40d9daef287f1d84498ea6b2acf66af55bdbd77e077f896"
hardening = ["vis"]
