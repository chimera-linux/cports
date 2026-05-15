pkgname = "newsraft"
pkgver = "0.36"
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
sha256 = "769dce748a4de741f1888eb199f71aeb41068b8527e0d5779fe0eb51fbbd72e3"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_file("doc/newsraft.desktop", "usr/share/applications")
    self.install_license("doc/license.txt")
