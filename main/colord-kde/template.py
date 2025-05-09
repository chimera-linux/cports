pkgname = "colord-kde"
pkgver = "25.04.1"
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
    "kcoreaddons-devel",
    "kdbusaddons-devel",
    "ki18n-devel",
    "kitemmodels-devel",
    "kwidgetsaddons-devel",
    "kwindowsystem-devel",
    "lcms2-devel",
    "qt6-qtdeclarative-devel",
]
pkgdesc = "KDE colord integration"
license = "GPL-2.0-or-later"
url = "https://invent.kde.org/graphics/colord-kde"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/colord-kde-{pkgver}.tar.xz"
sha256 = "e4bec245585d1a2a458e2c4164903fa981afe4a5fc905ccdfa355c4829f1a4bd"
hardening = ["vis"]
