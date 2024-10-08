pkgname = "kwayland"
pkgver = "6.2.0"
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
    "qt6-qtbase-devel",
    "qt6-qtwayland-devel",
    "wayland-protocols",
]
pkgdesc = "Qt-style Client and Server library wrapper for the Wayland libraries"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.1-only OR LGPL-3.0-only"
url = "https://invent.kde.org/frameworks/kwayland"
source = f"$(KDE_SITE)/plasma/{pkgver}/kwayland-{pkgver}.tar.xz"
sha256 = "7ffe0c2b1f82315b6226c50cfb752e6738e576fbf70b7296d1717b3d86226244"


@subpackage("kwayland-devel")
def _(self):
    return self.default_devel()
