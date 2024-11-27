pkgname = "print-manager"
pkgver = "6.2.4"
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
    "kdbusaddons-devel",
    "ki18n-devel",
    "kiconthemes-devel",
    "kio-devel",
    "kirigami-devel",
    "knotifications-devel",
    "kwidgetsaddons-devel",
    "kwindowsystem-devel",
    "libplasma-devel",
    "qt6-qt5compat-devel",
    "qt6-qtdeclarative-devel",
]
depends = ["cups"]
pkgdesc = "KDE tool for printers"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-or-later AND LGPL-2.0-or-later AND (LGPL-2.1-only OR LGPL-3.0-only)"
url = "https://invent.kde.org/plasma/print-manager"
source = f"$(KDE_SITE)/plasma/{pkgver}/print-manager-{pkgver}.tar.xz"
sha256 = "e0bcb91ad3b19e4259a7a35097f71879d2efe6d966521979033fb1e91fc6b895"
hardening = ["vis"]
