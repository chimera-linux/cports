pkgname = "oxygen-sounds"
pkgver = "6.2.4"
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
sha256 = "7967bc3920303725aae1b57001f2192b06a25084fbf3b8e845f5f051a56258de"
