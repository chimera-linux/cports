pkgname = "difftastic"
pkgver = "0.62.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = [
    "cargo-auditable",
]
makedepends = [
    "rust-std",
]
pkgdesc = "Structural diff tool"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "MIT"
url = "https://difftastic.wilfred.me.uk"
source = (
    f"https://github.com/Wilfred/difftastic/archive/refs/tags/{pkgver}.tar.gz"
)
sha256 = "ef69a23c6e3b9697d84ea5be158e8cb6d7482f49fc91cf4f9c7416bd48301260"


def post_install(self):
    self.install_license("LICENSE")
