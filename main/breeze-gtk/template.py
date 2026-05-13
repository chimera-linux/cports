pkgname = "breeze-gtk"
pkgver = "6.6.5"
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
sha256 = "76caad4ca2e3ce8b02ae1ebe0c068101bb07db51da47f88fa3a40cdce393abf6"
