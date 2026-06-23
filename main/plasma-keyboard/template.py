pkgname = "plasma-keyboard"
pkgver = "6.7.1"
pkgrel = 0
build_style = "cmake"
make_check_wrapper = ["wlheadless-run", "--"]
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
    "libplasma-devel",
    "qt6-qtbase-private-devel",
    "qt6-qtvirtualkeyboard-devel",
    "qt6-qtwayland-devel",
    "wayland-protocols",
]
checkdepends = ["xwayland-run"]
pkgdesc = "Plasma on-screen keyboard"
license = "GPL-2.0-or-later"
url = "https://invent.kde.org/plasma/plasma-keyboard"
source = f"$(KDE_SITE)/plasma/{pkgver}/plasma-keyboard-{pkgver}.tar.xz"
sha256 = "acf36a8d36150c6a0ecee2eeb0f70c4f1226cae3fedf47f38e06d765b6388047"
