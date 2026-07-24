pkgname = "kotofetch"
pkgver = "0.2.22"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Displays Japanese quotes in the terminal"
license = "MIT"
url = "https://github.com/hxpe-dev/kotofetch"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "0e04bedde86fcdd05b41e15211aa8459d24d347b3e45cf030383f5b650c01bf4"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
