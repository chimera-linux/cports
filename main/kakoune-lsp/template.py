pkgname = "kakoune-lsp"
pkgver = "18.1.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Kakoune language server protocol client"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT OR Unlicense"
url = "https://github.com/kakoune-lsp/kakoune-lsp"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "e9be8b132cc92612b5fa94535b0162b093bceacf20b6c883895acae0ef36eb8f"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/kak-lsp")
    self.install_license("MIT")
