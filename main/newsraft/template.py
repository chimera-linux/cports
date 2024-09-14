pkgname = "newsraft"
pkgver = "0.25"
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
sha256 = "99e587c8dcd22addd1dbd1f6f3a823af234a941009f016abbbf325ab5a6c44a0"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("doc/license.txt")
