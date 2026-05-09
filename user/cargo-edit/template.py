pkgname = "cargo-edit"
pkgver = "0.13.10"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["rust-std"]
pkgdesc = "CLI utility for managing cargo dependencies"
license = "Apache-2.0 OR MIT"
url = "https://github.com/killercup/cargo-edit"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "f0c085d9e25bbfea568baf521a199290eb95bf162ddca586a7f87b2634d9a573"
# Checks don't work with our cargo config overrides
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
