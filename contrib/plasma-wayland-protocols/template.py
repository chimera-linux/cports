pkgname = "plasma-wayland-protocols"
pkgver = "1.12.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
]
pkgdesc = "Plasma-specific wayland protocols"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT AND (LGPL-2.1-only OR LGPL-3.0-only)"
url = "https://invent.kde.org/libraries/plasma-wayland-protocols"
source = f"$(KDE_SITE)/plasma-wayland-protocols/plasma-wayland-protocols-{pkgver}.tar.xz"
sha256 = "1483bfd279cb913c83579b5d71c58f9958764f9ba4303b3647e1007cb70d4f9e"


def post_install(self):
    self.install_license("LICENSES/MIT.txt")
