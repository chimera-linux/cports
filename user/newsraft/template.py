pkgname = "newsraft"
pkgver = "0.35"
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
sha256 = "6a87c8a9b8556650d18443baf827cf930aa4a5c5361a36397b95f275e28d540d"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_file("doc/newsraft.desktop", "usr/share/applications")
    self.install_license("doc/license.txt")
