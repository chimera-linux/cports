pkgname = "newsraft"
pkgver = "0.38"
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
sha256 = "60da202448e104687c429a6d7b227ec7d038f7b906001dda594c78847efcc378"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("doc/license.txt")
