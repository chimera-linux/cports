pkgname = "kwayland"
pkgver = "6.7.91"
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
source = f"$(KDE_UNSTABLE_SITE)/plasma/{pkgver}/kwayland-{pkgver}.tar.xz"
sha256 = "3c36280c3ee6403f6385dc311e11684acff2fbc4dc215c6c2a211c814f308502"


@subpackage("kwayland-devel")
def _(self):
    return self.default_devel()
