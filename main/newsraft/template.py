pkgname = "newsraft"
pkgver = "0.31"
pkgrel = 0
build_style = "makefile"
hostmakedepends = ["pkgconf"]
makedepends = [
    "curl-devel",
    "gumbo-parser-devel",
    "libexpat-devel",
    "sqlite-devel",
]
pkgdesc = "Feed reader for terminal"
license = "ISC"
url = "https://codeberg.org/newsraft/newsraft"
source = f"{url}/archive/newsraft-{pkgver}.tar.gz"
sha256 = "de0d96664d9a276dbe58cf4b44a6861bc18b6fd4c0f41a97450c5b3509904ae8"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("doc/license.txt")
