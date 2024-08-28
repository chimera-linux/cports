pkgname = "texlab"
pkgver = "5.19.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "LaTeX LSP server"
maintainer = "ttyyls <contact@behri.org>"
license = "GPL-3.0-or-later"
url = "https://github.com/latex-lsp/texlab"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "ad72171dd267fd73ecc6a05f9ff3cc068e77a3b82f986305ab455aeade841294"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/texlab")
