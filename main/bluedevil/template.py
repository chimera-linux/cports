pkgname = "bluedevil"
pkgver = "6.5.4"
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
sha256 = "3813eee7879c8181cf16b5bc703b0565868edfdd062d9ec38479c406cbb324f1"
hardening = ["vis"]
