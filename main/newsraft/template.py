pkgname = "newsraft"
pkgver = "0.26"
pkgrel = 0
build_style = "makefile"
hostmakedepends = [
    "pkgconf",
    "scdoc",
]
makedepends = [
    "gumbo-parser-devel",
    "libcurl-devel",
    "libexpat-devel",
    "ncurses-devel",
    "sqlite-devel",
    "yajl-devel",
]
pkgdesc = "Feed reader for terminal"
maintainer = "ttyyls <contact@behri.org>"
license = "ISC"
url = "https://codeberg.org/newsraft/newsraft"
source = f"{url}/archive/newsraft-{pkgver}.tar.gz"
sha256 = "4c96ecb5628a14b7acabff4645595326b079ca1a93c2b2cbbd1af03aef1b91ea"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("doc/license.txt")
