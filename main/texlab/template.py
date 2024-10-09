pkgname = "texlab"
pkgver = "5.20.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "LaTeX LSP server"
maintainer = "ttyyls <contact@behri.org>"
license = "GPL-3.0-or-later"
url = "https://github.com/latex-lsp/texlab"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "7f110967b75ac0c50e773f5af5ad9b67c4544ca2545f43662f6ae7918ca5d9c6"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/texlab")
