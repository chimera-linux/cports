pkgname = "rust-audit-info"
pkgver = "0.5.2"
pkgrel = 0
build_wrksrc = "rust-audit-info"
build_style = "cargo"
hostmakedepends = ["cargo"]
makedepends = ["rust-std"]
pkgdesc = "CLI tool to extract dependency info embedded by cargo auditable"
maintainer = "Jan Christian Grünhage <jan.christian@gruenhage.xyz>"
license = "MIT OR Apache-2.0"
url = "https://github.com/rust-secure-code/cargo-auditable/tree/master/rust-audit-info"
source = f"https://github.com/rust-secure-code/cargo-auditable/archive/refs/tags/rust-audit-info/v{pkgver}.tar.gz"
sha256 = "d9bf684d1954db44e2f254e2fff5d204cb12e652ae95941abed9e10812786046"


def post_install(self):
    self.install_license("../LICENSE-MIT")
