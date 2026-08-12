pkgname = "plasma-keyboard"
pkgver = "6.7.4"
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
sha256 = "7bbcf6df3e4f3aa2f0c59e33fdc5cfc93377c04369283f1900be8f7b8fe194a1"
