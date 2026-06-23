# TODO: rename to sound-theme-ocean?
pkgname = "ocean-sound-theme"
pkgver = "6.7.1"
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
sha256 = "7ff1b7371fc63eaa9b98475095918030a9438aae67d32c66ee0cb4d72372d625"
