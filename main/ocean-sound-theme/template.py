# TODO: rename to sound-theme-ocean?
pkgname = "ocean-sound-theme"
pkgver = "6.3.4"
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
sha256 = "06317dac665aec586d2141237ac6c898d401c5659a4f0d98548b6b9019c4a1ec"
