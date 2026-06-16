pkgname = "plasma-wayland-protocols"
pkgver = "1.21.0"
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
sha256 = "698a7b28b711270314e396e248ae86087cfeaed01372009063995be6e1dc85ba"


def post_install(self):
    self.install_license("LICENSES/MIT.txt")
