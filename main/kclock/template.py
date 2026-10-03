pkgname = "kclock"
pkgver = "26.08.2"
pkgrel = 1
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
sha256 = "87118a36faa3c24dbec85769544d16f73a35fed65ef2afe11607ba6427d8107c"
hardening = ["vis"]
options = ["etcfiles"]
