# Keep in sync with cargo-auditable
pkgname = "cargo-auditable-bootstrap"
pkgver = "0.6.2"
pkgrel = 0
build_wrksrc = "cargo-auditable"
build_style = "cargo"
hostmakedepends = ["cargo"]
depends = ["cargo"]
pkgdesc = "Tool for embedding dependency information in rust binaries"
maintainer = "Jan Christian Grünhage <jan.christian@gruenhage.xyz>"
license = "Apache-2.0 OR MIT"
url = "https://github.com/rust-secure-code/cargo-auditable"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "b1c1455b5917d57d4beb3f9bf845059c2d701a034a060b908c7127e29e9b94f3"


def post_install(self):
    self.install_license("../LICENSE-MIT")
