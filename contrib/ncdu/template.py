pkgname = "ncdu"
pkgver = "1.20"
pkgrel = 1
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "pkgconf",
]
makedepends = ["ncurses-devel", "linux-headers"]
pkgdesc = "Disk usage analyzer with an ncurses interface"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://dev.yorhel.nl/ncdu"
source = f"https://dev.yorhel.nl/download/ncdu-{pkgver}.tar.gz"
sha256 = "5fe2bb841abe72374bb242dbb93293c4ae053078432d896a7481b2ff10be9572"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")
