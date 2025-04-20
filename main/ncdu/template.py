pkgname = "ncdu"
pkgver = "1.22"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "pkgconf",
]
makedepends = ["ncurses-devel", "linux-headers"]
pkgdesc = "Disk usage analyzer with an ncurses interface"
license = "MIT"
url = "https://dev.yorhel.nl/ncdu"
source = f"https://dev.yorhel.nl/download/ncdu-{pkgver}.tar.gz"
sha256 = "0ad6c096dc04d5120581104760c01b8f4e97d4191d6c9ef79654fa3c691a176b"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")
