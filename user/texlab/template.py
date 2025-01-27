pkgname = "texlab"
pkgver = "5.22.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "LaTeX LSP server"
maintainer = "ttyyls <contact@behri.org>"
license = "GPL-3.0-or-later"
url = "https://github.com/latex-lsp/texlab"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "dfca5bc12419e771092b6bdaf9379fe04164848ff19054d4ec7c4bba0eef7021"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/texlab")
