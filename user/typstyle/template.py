pkgname = "typstyle"
pkgver = "0.12.14"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Typst code formatter"
maintainer = "ttyyls <contact@behri.org>"
license = "Apache-2.0"
url = "https://github.com/Enter-tainer/typstyle"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "053ae2b6349fe244f44dc816f7d91036c152eeb14bfc2c6bfeeca33cc5ac0c34"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/typstyle")
