pkgname = "kio-zeroconf"
pkgver = "25.04.3"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBUILD_WITH_QT6=ON"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "kdbusaddons-devel",
    "kdnssd-devel",
    "ki18n-devel",
    "kio-devel",
    "qt6-qtdeclarative-devel",
]
pkgdesc = "KDE KIO zeroconf support"
license = "GPL-2.0-or-later AND LGPL-2.0-only"
url = "https://invent.kde.org/network/kio-zeroconf"
source = (
    f"$(KDE_SITE)/release-service/{pkgver}/src/kio-zeroconf-{pkgver}.tar.xz"
)
sha256 = "d651046859c84bc3591a2d88dafad0e47ad6489e25655aee23c1cf41667feac5"
hardening = ["vis"]
