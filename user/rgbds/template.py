pkgname = "rgbds"
pkgver = "0.9.3"
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
sha256 = "e4db822494e438f4a3619a0043280fec5a16596ac1dc7756e7c8bf1c57ab0376"
# No check or test targets
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
