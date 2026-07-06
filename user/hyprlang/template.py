pkgname = "hyprlang"
pkgver = "0.6.8"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "clang",
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = ["hyprutils-devel"]
pkgdesc = "Hypr configuration language"
license = "LGPL-3.0-only"
url = "https://github.com/hyprwm/hyprlang"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "d10a0778b646e04d83e8b90cc0f764fb96958c01a15c3c0678d95a40fc647ed5"


@subpackage("hyprlang-devel")
def _(self):
    return self.default_devel()
