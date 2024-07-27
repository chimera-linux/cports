pkgname = "cargo-edit"
pkgver = "0.12.3"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["openssl-devel", "libgit2-devel"]
pkgdesc = "CLI utility for managing cargo dependencies"
maintainer = "Jan Christian Grünhage <jan.christian@gruenhage.xyz>"
license = "Apache-2.0 OR MIT"
url = "https://github.com/killercup/cargo-edit"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "5ee14b3f16caa2f36d1e6d41f768043f134e552bec8dbe9d3afe00621b2d0020"
# Checks don't work with our cargo config overrides
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
