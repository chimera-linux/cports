pkgname = "bluedevil"
pkgver = "6.8.3"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
]
makedepends = [
    "bluez-qt-devel",
    "kcmutils-devel",
    "kcoreaddons-devel",
    "kdbusaddons-devel",
    "kdoctools-devel",
    "ki18n-devel",
    "kio-devel",
    "kirigami-devel",
    "knotifications-devel",
    "ksvg-devel",
    "kwidgetsaddons-devel",
    "kwindowsystem-devel",
    "libplasma-devel",
    "qt6-qtdeclarative-devel",
]
depends = ["kdeclarative"]
pkgdesc = "KDE Plasma Bluetooth integration"
license = "GPL-2.0-or-later AND LGPL-2.0-or-later"
url = "https://invent.kde.org/plasma/bluedevil"
source = f"$(KDE_SITE)/plasma/{pkgver}/bluedevil-{pkgver}.tar.xz"
sha256 = "52c3bdbe75f986b796fabf326c4414a07d0fecb5fb066844c5673c0b91fbb36b"
hardening = ["vis"]
# needs the kcm installed
options = ["!check"]
