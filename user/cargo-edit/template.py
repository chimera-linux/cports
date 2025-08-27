pkgname = "cargo-edit"
pkgver = "0.13.7"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["rust-std"]
pkgdesc = "CLI utility for managing cargo dependencies"
license = "Apache-2.0 OR MIT"
url = "https://github.com/killercup/cargo-edit"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "f242010b4b0b8ccd245693858d26a35f70bef572a209f4977d192c1215e861c6"
# Checks don't work with our cargo config overrides
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
