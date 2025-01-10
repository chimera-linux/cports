pkgname = "plasma-wayland-protocols"
pkgver = "1.16.0"
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
sha256 = "da3fbbe3fa5603f9dc9aabe948a6fc8c3b451edd1958138628e96c83649c1f16"


def post_install(self):
    self.install_license("LICENSES/MIT.txt")
