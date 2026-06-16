pkgname = "oxygen-sounds"
pkgver = "6.7.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
    "pkgconf",
]
makedepends = [
    "qt6-qtdeclarative-devel",
]
pkgdesc = "Ocean Sound Theme for KDE Plasma"
license = "CC-BY-SA-4.0"
url = "https://invent.kde.org/plasma/oxygen-sounds"
source = f"$(KDE_SITE)/plasma/{pkgver}/oxygen-sounds-{pkgver}.tar.xz"
sha256 = "62a3dd7a88a570d69c370a71a261c8dd04d92daf90250ca2a9d23c29e67e1c8a"
