pkgname = "plasma-wayland-protocols"
pkgver = "1.23.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
    "qt6-qtbase-devel",
    "wayland-progs",
]
makedepends = [
    "wayland-devel",
]
pkgdesc = "Plasma-specific wayland protocols"
license = "MIT AND (LGPL-2.1-only OR LGPL-3.0-only)"
url = "https://invent.kde.org/libraries/plasma-wayland-protocols"
source = f"$(KDE_SITE)/plasma-wayland-protocols/plasma-wayland-protocols-{pkgver}.tar.xz"
sha256 = "16c5ad917bde2ed795942dacba76654819ddc6a1566842325ef34e0b553ef138"


def post_install(self):
    self.install_license("LICENSES/MIT.txt")
