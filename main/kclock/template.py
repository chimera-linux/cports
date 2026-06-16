pkgname = "kclock"
pkgver = "26.04.2"
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
    "plasma-wayland-protocols",
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
sha256 = "9f5c998462316df456a7e9413b039300003f421e72ad40b3b393e43f6c958558"
hardening = ["vis"]
