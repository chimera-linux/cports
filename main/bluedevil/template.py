pkgname = "bluedevil"
pkgver = "6.7.91"
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
source = f"$(KDE_UNSTABLE_SITE)/plasma/{pkgver}/bluedevil-{pkgver}.tar.xz"
sha256 = "e7ccc777ef3553d2fc44a593056814894810dd69bd516c148b16a43fd98a8484"
hardening = ["vis"]
# needs the kcm installed
options = ["!check"]
