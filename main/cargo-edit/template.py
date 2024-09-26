pkgname = "cargo-edit"
pkgver = "0.13.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["rust-std"]
pkgdesc = "CLI utility for managing cargo dependencies"
maintainer = "Jan Christian Grünhage <jan.christian@gruenhage.xyz>"
license = "Apache-2.0 OR MIT"
url = "https://github.com/killercup/cargo-edit"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "c81a73fb1ef4ffef722835baf473beed9868ce2c58ad98a27596f2cbabbfcba3"
# Checks don't work with our cargo config overrides
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
