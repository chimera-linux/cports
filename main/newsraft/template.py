pkgname = "newsraft"
pkgver = "0.28"
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
maintainer = "ttyyls <contact@behri.org>"
license = "ISC"
url = "https://codeberg.org/newsraft/newsraft"
source = f"{url}/archive/newsraft-{pkgver}.tar.gz"
sha256 = "4314c6f5b278e52583bc3a48808ac7b4e7bbea9e992fafb19c4e30c8399bf025"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("doc/license.txt")
