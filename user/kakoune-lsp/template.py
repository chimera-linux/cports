pkgname = "kakoune-lsp"
pkgver = "22.0.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Kakoune language server protocol client"
license = "MIT OR Unlicense"
url = "https://github.com/kakoune-lsp/kakoune-lsp"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "fe631342dc68692ac8cf3ff454e83d37756998e85f27f33d0cfd923c1309a7e0"


def install(self):
    from cbuild.util import cargo

    self.install_bin(cargo.target_path(self, "kak-lsp"))
    self.install_license("MIT")
