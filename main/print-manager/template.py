pkgname = "print-manager"
pkgver = "6.7.2"
pkgrel = 0
build_style = "cmake"
make_check_args = ["-E", "pm-modeltests"]
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "kcmutils-devel",
    "kdbusaddons-devel",
    "kdeclarative-devel",
    "ki18n-devel",
    "kiconthemes-devel",
    "kio-devel",
    "kirigami-addons-devel",
    "kirigami-devel",
    "kitemmodels-devel",
    "knotifications-devel",
    "kwidgetsaddons-devel",
    "kwindowsystem-devel",
    "libplasma-devel",
    "qt6-qtdeclarative-devel",
]
pkgdesc = "KDE tool for printers"
license = "GPL-2.0-or-later AND LGPL-2.0-or-later AND (LGPL-2.1-only OR LGPL-3.0-only)"
url = "https://invent.kde.org/plasma/print-manager"
source = f"$(KDE_SITE)/plasma/{pkgver}/print-manager-{pkgver}.tar.xz"
sha256 = "a4c55001f104634012c8107faa3e12132ae4c8e30ab00b46b419ef0b0144ead1"
hardening = ["vis"]
