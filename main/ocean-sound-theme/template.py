# TODO: rename to sound-theme-ocean?
pkgname = "ocean-sound-theme"
pkgver = "6.4.2"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
]
makedepends = [
    "qt6-qtbase-devel",
]
pkgdesc = "Ocean Sound Theme for KDE Plasma"
license = "CC-BY-SA-4.0"
url = "https://invent.kde.org/plasma/ocean-sound-theme"
source = f"$(KDE_SITE)/plasma/{pkgver}/ocean-sound-theme-{pkgver}.tar.xz"
sha256 = "d1b45a1a563f88aea51cc1f63e3a5112084cbcd1f0384394eb8a8d91c5c8a466"
