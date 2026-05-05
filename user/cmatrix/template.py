pkgname = "cmatrix"
pkgver = "2.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DCMAKE_POLICY_VERSION_MINIMUM=3.5",
]
hostmakedepends = [
    "cmake",
    "kbd",
    "ninja",
    "pkgconf",
]
makedepends = ["ncurses-devel"]
pkgdesc = "Simulator for display from the Matrix"
license = "GPL-3.0-only"
url = "https://github.com/abishekvashok/cmatrix"
source = f"{url}/archive/refs/tags/v{pkgver}.zip"
sha256 = "82228753f9cf7d28cb9772010e70d6f5e13639fb0fd918b1006ed2c3b9ed0ab5"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("COPYING")
    self.install_man("cmatrix.1")
