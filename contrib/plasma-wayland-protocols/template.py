pkgname = "plasma-wayland-protocols"
pkgver = "1.13.0"
pkgrel = 1
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
]
pkgdesc = "Plasma-specific wayland protocols"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "MIT AND (LGPL-2.1-only OR LGPL-3.0-only)"
url = "https://invent.kde.org/libraries/plasma-wayland-protocols"
source = f"$(KDE_SITE)/plasma-wayland-protocols/plasma-wayland-protocols-{pkgver}.tar.xz"
sha256 = "dd477e352f5ff6e6ac686286c4b22b19bf5a4921b85ee5a7da02bb7aa115d57e"


def post_install(self):
    self.install_license("LICENSES/MIT.txt")
