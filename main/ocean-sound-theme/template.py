# TODO: rename to sound-theme-ocean?
pkgname = "ocean-sound-theme"
pkgver = "6.7.91"
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
source = (
    f"$(KDE_UNSTABLE_SITE)/plasma/{pkgver}/ocean-sound-theme-{pkgver}.tar.xz"
)
sha256 = "b7595a63e880d99236525b1dbc6de3a3076545aef41e7464ad05f41dd028abc6"
