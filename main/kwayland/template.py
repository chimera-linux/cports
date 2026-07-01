pkgname = "kwayland"
pkgver = "6.7.2"
pkgrel = 0
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
sha256 = "3d3ca745d4f7a53be8b331fccde825d9cc54a8761d7a33318f4fb2d602b857f4"


@subpackage("kwayland-devel")
def _(self):
    return self.default_devel()
