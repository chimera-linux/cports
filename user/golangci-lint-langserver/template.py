pkgname = "golangci-lint-langserver"
pkgver = "0.0.12"
pkgrel = 1
build_style = "go"
hostmakedepends = ["go"]
depends = ["golangci-lint"]
checkdepends = ["golangci-lint"]
pkgdesc = "Language server for golangci-lint"
license = "MIT"
url = "https://github.com/nametake/golangci-lint-langserver"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "bdda9b1138f0a6cbfec0b2a93ef64111410bf16a82583c659e1b57f11ed93936"


def post_install(self):
    self.install_license("LICENSE")
