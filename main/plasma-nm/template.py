pkgname = "plasma-nm"
pkgver = "6.4.1"
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
    "kcmutils-devel",
    "kcolorscheme-devel",
    "kcompletion-devel",
    "kcoreaddons-devel",
    "kdbusaddons-devel",
    "ki18n-devel",
    "kio-devel",
    "kirigami-devel",
    "knotifications-devel",
    "ksvg-devel",
    "kwallet-devel",
    "libplasma-devel",
    "modemmanager-qt-devel",
    "networkmanager-qt-devel",
    "prison-devel",
    "qca-devel",
    "qcoro-devel",
    "qt6-qtdeclarative-devel",
    # TODO: openconnect>=3.99 -> qt6-qtwebengine-devel
]
depends = ["prison"]
pkgdesc = "KDE Plasma NetworkManager integration"
license = "GPL-2.0-or-later AND LGPL-2.0-or-later"
url = "https://invent.kde.org/plasma/plasma-nm"
source = f"$(KDE_SITE)/plasma/{pkgver}/plasma-nm-{pkgver}.tar.xz"
sha256 = "51dc338e51d606e131f4e33d4fb7bb28ead8a49cd68a462252dc920a59111c50"
hardening = ["vis"]
