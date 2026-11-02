pkgname = "oxygen-sounds"
pkgver = "6.8.2"
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
sha256 = "89cfad4b243cdd6e031739566693df77ffdc7a29cedc10dad0b96507a2b3ea62"
