pkgname = "breeze-gtk"
pkgver = "6.2.4"
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
sha256 = "610c24d4686be08a92337516b67e9f09c7e365dddc3e02976d24af364233bca0"
