pkgname = "goawk"
pkgver = "1.29.1"
pkgrel = 9
build_style = "go"
hostmakedepends = ["go"]
checkdepends = ["gawk"]
pkgdesc = "POSIX-compliant implementation of Awk"
license = "MIT"
url = "https://github.com/benhoyt/goawk"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "9c355857faf7168f99e78d090ebe993ff10732a5ff34735cdc3e86256ce8c989"


def post_install(self):
    self.install_license("LICENSE.txt")
