pkgname = "kakoune-lsp"
pkgver = "18.0.3"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Kakoune language server protocol client"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT OR Unlicense"
url = "https://github.com/kakoune-lsp/kakoune-lsp"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "75de62446a3eabc0e96b170b5d9c18cd37dabcbfbaa2a9e50240a00dab271a93"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/kak-lsp")
    self.install_license("MIT")
