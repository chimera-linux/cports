pkgname = "kakoune-lsp"
pkgver = "18.0.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Kakoune language server protocol client"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT OR Unlicense"
url = "https://github.com/kakoune-lsp/kakoune-lsp"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "32473d84d6089abba0b022368aed3519b9dda86b4b840d5438eef20d0f452869"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/kak-lsp")
    self.install_license("MIT")
