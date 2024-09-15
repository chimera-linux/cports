pkgname = "goawk"
pkgver = "1.28.1"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
checkdepends = ["gawk"]
pkgdesc = "POSIX-compliant implementation of Awk"
maintainer = "Paul A. Patience <paul@apatience.com>"
license = "MIT"
url = "https://github.com/benhoyt/goawk"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "bed9009c2702fca12fe773e223d9f22bae9a26133d45c523bc3d598b2819b4cf"


def post_install(self):
    self.install_license("LICENSE.txt")
