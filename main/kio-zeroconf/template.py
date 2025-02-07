pkgname = "kio-zeroconf"
pkgver = "24.12.2"
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
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-or-later AND LGPL-2.0-only"
url = "https://invent.kde.org/network/kio-zeroconf"
source = (
    f"$(KDE_SITE)/release-service/{pkgver}/src/kio-zeroconf-{pkgver}.tar.xz"
)
sha256 = "d0ff7766c5bae08067c92bd3c853e8f37ab049d82d87af433d56efb90542bc0c"
hardening = ["vis"]
