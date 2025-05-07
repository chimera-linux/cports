pkgname = "newsraft"
pkgver = "0.30"
pkgrel = 0
build_style = "makefile"
hostmakedepends = [
    "pkgconf",
    "scdoc",
]
makedepends = [
    "gumbo-parser-devel",
    "curl-devel",
    "libexpat-devel",
    "ncurses-devel",
    "sqlite-devel",
]
pkgdesc = "Feed reader for terminal"
license = "ISC"
url = "https://codeberg.org/newsraft/newsraft"
source = f"{url}/archive/newsraft-{pkgver}.tar.gz"
sha256 = "5ae782d7eb19042cd05e260c8ec0fe4d0544e51716885a4b1e96a673576bd998"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("doc/license.txt")
