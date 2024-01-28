pkgname = "newsraft"
pkgver = "0.23"
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
sha256 = "22c835f56ff84a4aadc86d9e56a5d8e531cc966ff6a1404f0b3f8f1a1a0655dc"
hardening = ["vis", "cfi"]
# checks for rfc3339 compliance fail
# also the tests don't build with vis
options = ["!check"]


def post_install(self):
    self.install_license("doc/license.txt")
