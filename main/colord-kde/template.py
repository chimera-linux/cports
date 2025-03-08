pkgname = "colord-kde"
pkgver = "24.12.3"
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
sha256 = "5117c07516e0ca4db505447c4dac8f33df38ecc639bd96a240489a5b1033f659"
hardening = ["vis"]
