pkgname = "kwayland"
pkgver = "6.4.5"
pkgrel = 2
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
    "pkgconf",
]
makedepends = [
    "plasma-wayland-protocols",
    "qt6-qtbase-private-devel",  # qwaylandwindow_p.h
    "qt6-qtwayland-devel",
    "wayland-protocols",
]
pkgdesc = "Qt-style Client and Server library wrapper for the Wayland libraries"
license = "LGPL-2.1-only OR LGPL-3.0-only"
url = "https://invent.kde.org/frameworks/kwayland"
source = f"$(KDE_SITE)/plasma/{pkgver}/kwayland-{pkgver}.tar.xz"
sha256 = "0b875d9e7cc5bac4d97d3443ff4311533e0d8dad401af1244d4758a5fa5428f3"


@subpackage("kwayland-devel")
def _(self):
    return self.default_devel()
