pkgname = "golangci-lint-langserver"
pkgver = "0.0.9"
pkgrel = 3
build_style = "go"
hostmakedepends = ["go"]
depends = ["golangci-lint"]
pkgdesc = "Language server for golangci-lint"
maintainer = "Denis Strizhkin <strdenis02@gmail.com>"
license = "MIT"
url = "https://github.com/nametake/golangci-lint-langserver"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "ad7241d271b9b46b6fc784ab1d035c322bd6ae44938514d69f5ad516a1a9fbfd"


def post_install(self):
    self.install_license("LICENSE")
