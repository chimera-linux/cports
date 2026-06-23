pkgname = "print-manager"
pkgver = "6.7.1"
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
sha256 = "63bbebeeded45fdead0c3b70fc8166fb3ad21dd7ab2a97cdcd37a8daa3b4c429"
hardening = ["vis"]
