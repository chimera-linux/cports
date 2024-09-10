pkgname = "oxygen-sounds"
pkgver = "6.1.5"
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
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "CC-BY-SA-4.0"
url = "https://invent.kde.org/plasma/oxygen-sounds"
source = f"$(KDE_SITE)/plasma/{pkgver}/oxygen-sounds-{pkgver}.tar.xz"
sha256 = "6690a49e22d15a6a6882b87f725a9da3bc496177b89a3952b01555a98bb446a5"
