pkgname = "newsraft"
pkgver = "0.22"
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
sha256 = "16dbda602a37a2c8052421e90dd00ca065bab4130c6c2c16d5ca2a8a184990b9"
hardening = ["vis", "cfi"]
# checks for rfc3339 compliance fail
# also the tests don't build with vis
options = ["!check"]


def post_install(self):
    self.install_license("doc/license.txt")
