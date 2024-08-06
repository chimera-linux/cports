pkgname = "oxygen-sounds"
pkgver = "6.1.4"
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
sha256 = "6875e9984ce19c79ec199f6e8eed1fd85a088a78669710a88f612b582aa341c9"
