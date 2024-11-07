pkgname = "goawk"
pkgver = "1.29.0"
pkgrel = 1
build_style = "go"
hostmakedepends = ["go"]
checkdepends = ["gawk"]
pkgdesc = "POSIX-compliant implementation of Awk"
maintainer = "Paul A. Patience <paul@apatience.com>"
license = "MIT"
url = "https://github.com/benhoyt/goawk"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "91bf708ad6776bea7e1fbd1a0969042de8ebc3139b89468a2a1f5405f3401f54"


def post_install(self):
    self.install_license("LICENSE.txt")
