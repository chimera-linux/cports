pkgname = "ncdu"
pkgver = "1.19"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "autoconf",
    "automake",
    "pkgconf",
]
makedepends = ["ncurses-devel", "linux-headers"]
pkgdesc = "Disk usage analyzer with an ncurses interface"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://dev.yorhel.nl/ncdu"
source = f"https://dev.yorhel.nl/download/ncdu-{pkgver}.tar.gz"
sha256 = "30363019180cde0752c7fb006c12e154920412f4e1b5dc3090654698496bb17d"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")
