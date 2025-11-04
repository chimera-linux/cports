pkgname = "kotofetch"
pkgver = "0.2.12"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Displays Japanese quotes in the terminal"
license = "MIT"
url = "https://github.com/hxpe-dev/kotofetch"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "80b143e5a087b2633d34012691c1446218b7ac8145a6df0ca66aba8514f9b2c9"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
