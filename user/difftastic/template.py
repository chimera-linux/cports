pkgname = "difftastic"
pkgver = "0.64.0"
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
sha256 = "54c7c93309ff9a2cbe87153ac1d16e80bacac4042c80f6b7206e9b71a6f10d0b"


def post_install(self):
    self.install_license("LICENSE")
