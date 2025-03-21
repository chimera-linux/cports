pkgname = "plasma-wayland-protocols"
pkgver = "1.17.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
    "wayland-progs",
]
makedepends = [
    "wayland-devel",
]
pkgdesc = "Plasma-specific wayland protocols"
license = "MIT AND (LGPL-2.1-only OR LGPL-3.0-only)"
url = "https://invent.kde.org/libraries/plasma-wayland-protocols"
source = f"$(KDE_SITE)/plasma-wayland-protocols/plasma-wayland-protocols-{pkgver}.tar.xz"
sha256 = "cbd44b440e6b7cc76b650da93a870897e5a94adf7882b19fdf8fe222d4f74a4f"


def post_install(self):
    self.install_license("LICENSES/MIT.txt")
