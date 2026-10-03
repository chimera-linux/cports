pkgname = "oxygen-sounds"
pkgver = "6.7.91"
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
source = f"$(KDE_UNSTABLE_SITE)/plasma/{pkgver}/oxygen-sounds-{pkgver}.tar.xz"
sha256 = "65e06bb888fd03df1d7dbb60097e414ff4717a83d3c89247fe60f143bc3926cb"
