pkgname = "goawk"
pkgver = "1.26.0"
pkgrel = 1
build_style = "go"
hostmakedepends = ["go"]
checkdepends = ["gawk"]
pkgdesc = "POSIX-compliant implementation of Awk"
maintainer = "Paul A. Patience <paul@apatience.com>"
license = "MIT"
url = "https://github.com/benhoyt/goawk"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "d1618e454e01f83ec9ee553f8955a805417bb49bb1449059d4f1cd037556b4ff"
options = ["!debug"]


def post_install(self):
    self.install_license("LICENSE.txt")
