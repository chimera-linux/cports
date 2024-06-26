pkgname = "kwayland"
pkgver = "6.1.1"
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
sha256 = "dc91d4afb73bdb3eab605285a10258903e3c115a9872ac0ba792cef4688fdb85"


@subpackage("kwayland-devel")
def _devel(self):
    return self.default_devel()
