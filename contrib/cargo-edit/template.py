pkgname = "cargo-edit"
pkgver = "0.12.2"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo", "pkgconf"]
makedepends = ["openssl-devel", "libgit2-devel"]
pkgdesc = "CLI utility for managing cargo dependencies"
maintainer = "Jan Christian Grünhage <jan.christian@gruenhage.xyz>"
license = "Apache-2.0 OR MIT"
url = "https://github.com/killercup/cargo-edit"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "10c86ca7585852ce288a44608ef87c827f4b733a94eb847ab15735b823b30560"
# Checks don't work with our cargo config overrides
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
