pkgname = "ncdu"
pkgver = "1.18.1"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "autoconf",
    "automake",
    "pkgconf",
]
makedepends = ["ncurses-devel"]
pkgdesc = "Disk usage analyzer with an ncurses interface"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://dev.yorhel.nl/ncdu"
source = f"https://dev.yorhel.nl/download/ncdu-{pkgver}.tar.gz"
sha256 = "7c0fa1eb29d85aaed4ba174164bdbb8f011b5c390d017c57d668fc7231332405"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")
