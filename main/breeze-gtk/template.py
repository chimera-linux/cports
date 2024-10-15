pkgname = "breeze-gtk"
pkgver = "6.2.1"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "breeze",
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "sassc",
    "python-cairo",
]
makedepends = ["breeze-devel", "qt6-qtbase-devel"]
pkgdesc = "KDE Breeze widget theme for GTK"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "CC0-1.0"
url = "https://invent.kde.org/plasma/breeze-gtk"
source = f"$(KDE_SITE)/plasma/{pkgver}/breeze-gtk-{pkgver}.tar.xz"
sha256 = "8b5478d6b705683f0c2c075ce83e1137ad97ed644d1a339d8f982c4dc123ef0e"
