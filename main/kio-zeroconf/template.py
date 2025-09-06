pkgname = "kio-zeroconf"
pkgver = "25.08.0"
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
sha256 = "23590d1773a80bf6156aebb1f9680a122df4edac14877c2b9697b4c3aad913b0"
hardening = ["vis"]
