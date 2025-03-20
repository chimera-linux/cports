pkgname = "kakoune-lsp"
pkgver = "18.1.3"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Kakoune language server protocol client"
license = "MIT OR Unlicense"
url = "https://github.com/kakoune-lsp/kakoune-lsp"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "b819358d0f0972c499aa3fbe7841fcc356b710b99653ea864c6905c8c26ce2df"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/kak-lsp")
    self.install_license("MIT")
