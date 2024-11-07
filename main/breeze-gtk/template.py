pkgname = "breeze-gtk"
pkgver = "6.2.3"
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
sha256 = "3c59b2f6059b6661ef1feb74e59ad305bad391d692b30d7d3b1e0d91c412c6a1"
