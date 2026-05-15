pkgname = "difftastic"
pkgver = "0.69.0"
pkgrel = 0
build_style = "cargo"
prepare_after_patch = True
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
sha256 = "49d722fb80a0324ea99fe11907f796cde635443084d15cc6f1afd9e0de54bde0"


def post_install(self):
    self.install_license("LICENSE")
