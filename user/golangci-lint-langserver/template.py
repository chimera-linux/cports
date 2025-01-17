pkgname = "golangci-lint-langserver"
pkgver = "0.0.10"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
depends = ["golangci-lint"]
checkdepends = ["golangci-lint"]
pkgdesc = "Language server for golangci-lint"
maintainer = "Denis Strizhkin <strdenis02@gmail.com>"
license = "MIT"
url = "https://github.com/nametake/golangci-lint-langserver"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "65c2ffa9b71da3fe7298d4b86ae5cd64108bdc8313026d9613f19956d5855abc"


def post_install(self):
    self.install_license("LICENSE")
