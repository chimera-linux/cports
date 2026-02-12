pkgname = "gofumpt"
pkgver = "0.9.2"
pkgrel = 2
build_style = "go"
make_build_args = [f"-ldflags= -X main.version=v{pkgver}"]
hostmakedepends = ["go"]
pkgdesc = "Stricter gofmt"
license = "BSD-3-Clause"
url = "https://github.com/mvdan/gofumpt"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "acff9518cf4ad3550ca910b9254fc8a706494d6a105fe2e92948fedc52a42a5b"
# needs net
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
    self.install_license("LICENSE.google")
