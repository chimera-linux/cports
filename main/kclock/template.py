pkgname = "kclock"
pkgver = "26.08.0"
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
sha256 = "4c104afa591021de9a69f780e274a6c0c66d1db1744d86f3b2838e1f26d48d80"
hardening = ["vis"]
options = ["etcfiles"]
