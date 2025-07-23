pkgname = "newsraft"
pkgver = "0.32"
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
sha256 = "a3b5f4935189316b5962658f29669472798a3e40d62b4f60d66644af3f04d2d3"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("doc/license.txt")
