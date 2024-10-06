pkgname = "newsraft"
pkgver = "0.27"
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
sha256 = "627b274901e5c3298d430f5adfedbd69b09de365ffeb18e768f091738fe39089"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("doc/license.txt")
