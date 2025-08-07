pkgname = "gofumpt"
pkgver = "0.8.0"
pkgrel = 2
build_style = "go"
make_build_args = [f"-ldflags= -X main.version=v{pkgver}"]
hostmakedepends = ["go"]
pkgdesc = "Stricter gofmt"
license = "BSD-3-Clause"
url = "https://github.com/mvdan/gofumpt"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "4e0e23832e74779ca0fa6af8ca7c15dbf20599dec34c8c96607b9b2e59157cb7"
# needs net
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
    self.install_license("LICENSE.google")
