# TODO: rename to sound-theme-ocean?
pkgname = "ocean-sound-theme"
pkgver = "6.0.5"
pkgrel = 1
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
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "CC-BY-SA-4.0"
url = "https://invent.kde.org/plasma/ocean-sound-theme"
source = f"$(KDE_SITE)/plasma/{pkgver}/ocean-sound-theme-{pkgver}.tar.xz"
sha256 = "6015f3931a74134fdd7eef5c7c7592ef8b740fcc084d7726f8df993dc5289f6b"
