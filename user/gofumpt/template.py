pkgname = "gofumpt"
pkgver = "0.9.1"
pkgrel = 0
build_style = "go"
make_build_args = [f"-ldflags= -X main.version=v{pkgver}"]
hostmakedepends = ["go"]
pkgdesc = "Stricter gofmt"
license = "BSD-3-Clause"
url = "https://github.com/mvdan/gofumpt"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "43cc77a94f65b2ba940310ac4268567d61b9cc01414b0c70cce45c5a60c8e4ec"
# needs net
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
    self.install_license("LICENSE.google")
