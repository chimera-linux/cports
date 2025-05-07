# TODO: rename to sound-theme-ocean?
pkgname = "ocean-sound-theme"
pkgver = "6.3.5"
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
sha256 = "e6ab2ef12ba392cdadbc4fa1043a4a1d5419b6177a086822f68c7a5b521798c3"
