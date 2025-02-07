pkgname = "kclock"
pkgver = "24.12.2"
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
sha256 = "0aecf0d33d97e3fe6f69588dbe2f2a771237072418a00c8a83c1755fc47a2a45"
hardening = ["vis"]
