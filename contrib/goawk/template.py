pkgname = "goawk"
pkgver = "1.27.0"
pkgrel = 2
build_style = "go"
hostmakedepends = ["go"]
checkdepends = ["gawk"]
pkgdesc = "POSIX-compliant implementation of Awk"
maintainer = "Paul A. Patience <paul@apatience.com>"
license = "MIT"
url = "https://github.com/benhoyt/goawk"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "f39d5b3ff50f3c16cbfaaa40eb01ec045092afa66988e9728661c65c0e5d6a93"
options = ["!debug"]


def post_install(self):
    self.install_license("LICENSE.txt")
