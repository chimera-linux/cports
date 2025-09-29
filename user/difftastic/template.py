pkgname = "difftastic"
pkgver = "0.65.0"
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
sha256 = "59462f69e2cedfdc1bee4fd0da48fe9a7ae635cdb6818c1a300b31c0b146d4b8"


def post_install(self):
    self.install_license("LICENSE")
