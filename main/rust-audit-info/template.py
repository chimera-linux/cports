pkgname = "rust-audit-info"
pkgver = "0.5.4"
pkgrel = 0
build_wrksrc = "rust-audit-info"
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "CLI tool to extract dependency info embedded by cargo auditable"
maintainer = "Jan Christian Grünhage <jan.christian@gruenhage.xyz>"
license = "MIT OR Apache-2.0"
url = "https://github.com/rust-secure-code/cargo-auditable/tree/master/rust-audit-info"
source = f"https://github.com/rust-secure-code/cargo-auditable/archive/refs/tags/rust-audit-info/v{pkgver}.tar.gz"
sha256 = "d9d53352b5f2dc34a93b1ae6408cdd50085f40e24d832af6938e0c3b7c906ff5"


def post_install(self):
    self.install_license("../LICENSE-MIT")
