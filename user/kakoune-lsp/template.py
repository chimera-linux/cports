pkgname = "kakoune-lsp"
pkgver = "21.0.2"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Kakoune language server protocol client"
license = "MIT OR Unlicense"
url = "https://github.com/kakoune-lsp/kakoune-lsp"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "34b4718af5ee39a05a1a176a25cdde4333d2de548e84c148389552e893bc7cc0"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/kak-lsp")
    self.install_license("MIT")
