pkgname = "kclock"
pkgver = "25.12.1"
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
    "kconfig-devel",
    "kcoreaddons-devel",
    "kcrash-devel",
    "kdbusaddons-devel",
    "ki18n-devel",
    "kio-devel",
    "kirigami-addons-devel",
    "kirigami-devel",
    "knotifications-devel",
    "kstatusnotifieritem-devel",
    "ksvg-devel",
    "libplasma-devel",
    "qt6-qtbase-private-devel",
    "qt6-qtmultimedia-devel",
    "qt6-qtsvg-devel",
    "wayland-protocols",
]
depends = ["kirigami-addons"]
pkgdesc = "KDE clock"
license = "GPL-3.0-or-later AND LGPL-2.1-or-later"
url = "https://apps.kde.org/kclock"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kclock-{pkgver}.tar.xz"
sha256 = "e0367d9a089d262844c4e925dd7a1b39057e2584b786fc640a603edf2e723335"
hardening = ["vis"]
