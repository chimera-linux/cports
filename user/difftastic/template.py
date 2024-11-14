pkgname = "difftastic"
pkgver = "0.61.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = [
    "cargo",
]
makedepends = [
    "rust-std",
]
pkgdesc = "Structural diff tool"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://difftastic.wilfred.me.uk"
source = (
    f"https://github.com/Wilfred/difftastic/archive/refs/tags/{pkgver}.tar.gz"
)
sha256 = "8e85001e32f1fe7b2c6d164f3a654cb589c6e48b6350421df27a56919da7a185"


def post_install(self):
    self.install_license("LICENSE")
