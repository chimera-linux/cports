pkgname = "texlab"
pkgver = "5.23.1"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "LaTeX LSP server"
license = "GPL-3.0-or-later"
url = "https://github.com/latex-lsp/texlab"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "32620d4a186222cef1140250c9c43b83ed873a4710d05a0075c7d8f6d1d4e1ec"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/texlab")
