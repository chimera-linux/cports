pkgname = "breeze-gtk"
pkgver = "6.2.2"
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
sha256 = "7cc23494b450d1979a86e1f5610cda5e798e24e174e820a25131014c78cb24a1"
