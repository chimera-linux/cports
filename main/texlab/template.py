pkgname = "texlab"
pkgver = "5.21.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "LaTeX LSP server"
maintainer = "ttyyls <contact@behri.org>"
license = "GPL-3.0-or-later"
url = "https://github.com/latex-lsp/texlab"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "723099514ffb7a6537f486de951ae2cfd97d2ae6420aa1ff8eb6ed4068ecb160"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/texlab")
