pkgname = "newsraft"
pkgver = "0.24"
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
source = f"{url}/archive/{pkgname}-{pkgver}.tar.gz"
sha256 = "1bc072350cee8960880cef0f749922c9474d91c9df467a0645b1632fbddb48f5"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("doc/license.txt")
