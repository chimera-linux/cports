pkgname = "newsraft"
pkgver = "0.34"
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
sha256 = "8d55441ddfc2e7d49ad3ff36c384ad4c1533de97d92a9fcaf3f6753b49b37c7c"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("doc/license.txt")
