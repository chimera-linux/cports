pkgname = "difftastic"
pkgver = "0.63.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = [
    "cargo-auditable",
]
makedepends = [
    "rust-std",
]
pkgdesc = "Structural diff tool"
license = "MIT"
url = "https://difftastic.wilfred.me.uk"
source = (
    f"https://github.com/Wilfred/difftastic/archive/refs/tags/{pkgver}.tar.gz"
)
sha256 = "f96bcf4fc961921d52cd9fe5aa94017924abde3d5a3b5a4727b103e9c2d4b416"


def post_install(self):
    self.install_license("LICENSE")
