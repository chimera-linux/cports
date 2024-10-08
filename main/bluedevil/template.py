pkgname = "bluedevil"
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
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-or-later AND LGPL-2.0-or-later"
url = "https://invent.kde.org/plasma/bluedevil"
source = f"$(KDE_SITE)/plasma/{pkgver}/bluedevil-{pkgver}.tar.xz"
sha256 = "8e3e71301734d22c84a1ff5c10c81fa52a50bf47ed2bf493fe05a88bfcbd1e7b"
hardening = ["vis"]
