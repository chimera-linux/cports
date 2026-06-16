pkgname = "plasma-keyboard"
pkgver = "6.6.5"
pkgrel = 1
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "kcmutils-devel",
    "kcoreaddons-devel",
    "kcrash-devel",
    "ki18n-devel",
    "qt6-qtbase-private-devel",
    "qt6-qtvirtualkeyboard-devel",
    "wayland-protocols",
]
pkgdesc = "Plasma on-screen keyboard"
license = "GPL-2.0-or-later"
url = "https://invent.kde.org/plasma/plasma-keyboard"
source = f"$(KDE_SITE)/plasma/{pkgver}/plasma-keyboard-{pkgver}.tar.xz"
sha256 = "3bb8be109cc449af54d03f28cc1c1a9e4d4150cb01b9af916a5516ed64740671"
