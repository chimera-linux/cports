pkgname = "polkit-qt-1"
pkgver = "0.201.1"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DQT_MAJOR_VERSION=6"]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "glib-devel",
    "polkit-devel",
    "qt6-qtbase-devel",
]
pkgdesc = "Qt wrapper around polkit-1 client libraries"
license = "LGPL-2.0-or-later"
url = "https://invent.kde.org/libraries/polkit-qt-1"
source = f"$(KDE_SITE)/polkit-qt-1/polkit-qt-1-{pkgver}.tar.xz"
sha256 = "95d8e2cae530c546d9437459deb8a1bea38d572f0f9772cc2860dc143637f256"
hardening = ["vis"]


@subpackage("polkit-qt-1-devel")
def _(self):
    return self.default_devel()
