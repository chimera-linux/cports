pkgname = "plasma-wayland-protocols"
pkgver = "1.15.0"
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
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "MIT AND (LGPL-2.1-only OR LGPL-3.0-only)"
url = "https://invent.kde.org/libraries/plasma-wayland-protocols"
source = f"$(KDE_SITE)/plasma-wayland-protocols/plasma-wayland-protocols-{pkgver}.tar.xz"
sha256 = "e5aedfe7c0b2443aa67882b4792d08814570e00dd82f719a35c922a0993f621e"


def post_install(self):
    self.install_license("LICENSES/MIT.txt")
