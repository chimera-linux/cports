pkgname = "scc"
pkgver = "3.6.0"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "Fast and accurate code counter"
license = "MIT OR Unlicense"
url = "https://github.com/boyter/scc"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "15e09f446ee44f3ebdb59f55933128256588d0343988692f1064b9bfb4f96dd7"


def post_install(self):
    self.install_license("LICENSE")
