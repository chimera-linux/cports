pkgname = "kclock"
pkgver = "24.08.2"
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
    "kdbusaddons-devel",
    "ki18n-devel",
    "kirigami-addons-devel",
    "kirigami-devel",
    "knotifications-devel",
    "kstatusnotifieritem-devel",
    "libplasma-devel",
    "qt6-qtmultimedia-devel",
    "qt6-qtsvg-devel",
]
depends = ["kirigami-addons"]
pkgdesc = "KDE clock"
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-3.0-or-later AND LGPL-2.1-or-later"
url = "https://apps.kde.org/kclock"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kclock-{pkgver}.tar.xz"
sha256 = "bc4fe69fca16b50725cb95b4711cc1b21cf8c5f023bf74d9d7f025b5c696f628"
hardening = ["vis"]
