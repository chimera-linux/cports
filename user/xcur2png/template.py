pkgname = "xcur2png"
pkgver = "0.7.1"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "pkgconf",
]
makedepends = [
    "libpng-devel",
    "libxcursor-devel",
]
pkgdesc = "Convert X cursors to PNG images"
license = "GPL-3.0-or-later"
url = "https://github.com/eworm-de/xcur2png"
source = f"{url}/releases/download/{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "bc6a062fdb48615a7159ed56ef3d2011168cd8a9decaf1d8a4e316d3064132c9"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_man("xcur2png.1")
