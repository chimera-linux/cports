pkgname = "texlab"
pkgver = "5.23.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "LaTeX LSP server"
license = "GPL-3.0-or-later"
url = "https://github.com/latex-lsp/texlab"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "f14a3e100706cc217a6720057dea2e30b7c7a3a7297e6d28ea741a533500a1cf"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/texlab")
