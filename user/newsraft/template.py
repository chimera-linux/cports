pkgname = "newsraft"
pkgver = "0.37"
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
sha256 = "725fdbf4c14d87eb7e926aebd9b116f540dca812bea02e73078070156d986ad4"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_file("doc/newsraft.desktop", "usr/share/applications")
    self.install_license("doc/license.txt")
