pkgname = "newsraft"
pkgver = "0.29"
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
    "yajl-devel",
]
pkgdesc = "Feed reader for terminal"
license = "ISC"
url = "https://codeberg.org/newsraft/newsraft"
source = f"{url}/archive/newsraft-{pkgver}.tar.gz"
sha256 = "71c29e98b71dd48e445449a689ad9a5b25e56eb294cd79c7ed5627d36eda6769"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("doc/license.txt")
