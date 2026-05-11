pkgname = "qrca"
pkgver = "26.04.1"
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
    "kcontacts-devel",
    "kcrash-devel",
    "kdbusaddons-devel",
    "ki18n-devel",
    "kio-devel",
    "kirigami-addons-devel",
    "kirigami-devel",
    "knotifications-devel",
    "kservice-devel",
    "networkmanager-qt-devel",
    "prison-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qtmultimedia-devel",
    "qt6-qtsvg-devel",
]
pkgdesc = "KDE QR code scanner"
license = "GPL-3.0-or-later"
url = "https://apps.kde.org/qrca"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/qrca-{pkgver}.tar.xz"
sha256 = "ec5be06ec59354b8f061fa5a46aabfa90aa8f0b2c821f15617a2bcec3282be8f"
hardening = ["vis"]
