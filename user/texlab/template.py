pkgname = "texlab"
pkgver = "5.26.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "LaTeX LSP server"
license = "GPL-3.0-or-later"
url = "https://github.com/latex-lsp/texlab"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "47af7e71247fe186ddbaa62373ce5fbebc802ab8df9924958ac62788a644f84e"


def install(self):
    from cbuild.util import cargo

    self.install_bin(cargo.target_path(self, "texlab"))
