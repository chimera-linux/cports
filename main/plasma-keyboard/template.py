pkgname = "plasma-keyboard"
pkgver = "6.7.5"
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
sha256 = "0dd91212308e6c6999db55b95b5b462cadc2766935272e9caf2f138b9a063788"
