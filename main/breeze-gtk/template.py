pkgname = "breeze-gtk"
pkgver = "6.7.2"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "breeze",
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "python-cairo",
    "sassc",
]
makedepends = ["breeze-devel", "qt6-qtbase-devel"]
pkgdesc = "KDE Breeze widget theme for GTK"
license = "CC0-1.0"
url = "https://invent.kde.org/plasma/breeze-gtk"
source = f"$(KDE_SITE)/plasma/{pkgver}/breeze-gtk-{pkgver}.tar.xz"
sha256 = "b5f15489ccd3159395f2828043c893035d8c0b4a18b050d188bbea8b6a5a99c5"
