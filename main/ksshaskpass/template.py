pkgname = "ksshaskpass"
pkgver = "6.3.4"
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
    "kcoreaddons-devel",
    "kdoctools-devel",
    "ki18n-devel",
    "kwallet-devel",
    "kwidgetsaddons-devel",
    "qt6-qtdeclarative-devel",
]
pkgdesc = "KDE askpass helper"
license = "GPL-2.0-or-later"
url = "https://invent.kde.org/plasma/ksshaskpass"
source = f"$(KDE_SITE)/plasma/{pkgver}/ksshaskpass-{pkgver}.tar.xz"
sha256 = "793341db12cf38ecece998ccbbb685871be5e5099ae6c886872279433a255995"
