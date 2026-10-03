pkgname = "print-manager"
pkgver = "6.7.91"
pkgrel = 0
build_style = "cmake"
make_check_args = ["-E", "(pm-modeltests|print-queue_smoketest)"]
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
source = f"$(KDE_UNSTABLE_SITE)/plasma/{pkgver}/print-manager-{pkgver}.tar.xz"
sha256 = "6e7c2ebe538f81bd658ac04dec8b713ec40046fbee4866f0d99d4f325a05c11c"
hardening = ["vis"]
