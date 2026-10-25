pkgname = "cargo-edit"
pkgver = "0.13.14"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["rust-std"]
pkgdesc = "CLI utility for managing cargo dependencies"
license = "Apache-2.0 OR MIT"
url = "https://github.com/killercup/cargo-edit"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "52f49ea8f76e2caa48d3b57bbcdfe1768268f25ad9a1f07878d9c670488180fb"
# Checks don't work with our cargo config overrides
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE-MIT")
