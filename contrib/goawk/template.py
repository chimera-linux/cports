pkgname = "goawk"
pkgver = "1.25.0"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
checkdepends = ["gawk"]
pkgdesc = "POSIX-compliant implementation of Awk"
maintainer = "Paul A. Patience <paul@apatience.com>"
license = "MIT"
url = "https://github.com/benhoyt/goawk"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "9d76415c6ce54c676428aa946ae1c4bc93863a3c680c8137711e65192628d7a2"
options = ["!debug"]


def post_install(self):
    self.install_license("LICENSE.txt")
