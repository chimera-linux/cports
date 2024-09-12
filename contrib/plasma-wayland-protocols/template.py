pkgname = "plasma-wayland-protocols"
pkgver = "1.14.0"
pkgrel = 0
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
sha256 = "1a4385ecfc79f7589f07381cab11c3ff51f6e2fa4b73b78600d6ad096394bf81"


def post_install(self):
    self.install_license("LICENSES/MIT.txt")
