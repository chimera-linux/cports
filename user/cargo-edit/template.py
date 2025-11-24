pkgname = "cargo-edit"
pkgver = "0.13.8"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["rust-std"]
pkgdesc = "CLI utility for managing cargo dependencies"
license = "Apache-2.0 OR MIT"
url = "https://github.com/killercup/cargo-edit"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "73bfbd80c0f54bffd8ebdfeb579ba8bd0ba4be9fdad06ed0f8dc99d3911f4774"
# Checks don't work with our cargo config overrides
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
