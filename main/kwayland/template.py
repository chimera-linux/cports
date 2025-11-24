pkgname = "kwayland"
pkgver = "6.5.3"
pkgrel = 1
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
sha256 = "e6c13b7a4812724102fe2f82f502e42f8812114381a82bb81b8613ea5ab38725"


@subpackage("kwayland-devel")
def _(self):
    return self.default_devel()
