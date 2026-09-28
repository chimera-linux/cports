pkgname = "rgbds"
pkgver = "0.9.4"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "bison",
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "libpng-devel",
]
pkgdesc = "Assembler/linker for the Game Boy and Game Boy Color"
license = "MIT"
url = "https://rgbds.gbdev.io"
source = f"https://github.com/gbdev/rgbds/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "29a0bdea2c07ae7e7af9f313de5deaa3ab0557e0251eac9b1e418cc18ebc0ba4"
# No check or test targets
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
