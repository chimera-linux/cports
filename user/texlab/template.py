pkgname = "texlab"
pkgver = "5.22.1"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "LaTeX LSP server"
maintainer = "ttyyls <contact@behri.org>"
license = "GPL-3.0-or-later"
url = "https://github.com/latex-lsp/texlab"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "dd7602c069e8411c1a744d5b25f80686339ef18e6f12c1bc971f27912e3e9714"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/texlab")
