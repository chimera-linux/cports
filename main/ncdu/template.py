pkgname = "ncdu"
pkgver = "1.21"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "pkgconf",
]
makedepends = ["ncurses-devel", "linux-headers"]
pkgdesc = "Disk usage analyzer with an ncurses interface"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "MIT"
url = "https://dev.yorhel.nl/ncdu"
source = f"https://dev.yorhel.nl/download/ncdu-{pkgver}.tar.gz"
sha256 = "a894d3a9b46bce578a6039bef48f54533ec402fb589b0769bfbb1d1edf9601a6"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")
