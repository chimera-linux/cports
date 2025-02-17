pkgname = "typstyle"
pkgver = "0.12.15"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Typst code formatter"
maintainer = "ttyyls <contact@behri.org>"
license = "Apache-2.0"
url = "https://github.com/Enter-tainer/typstyle"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "13e482cb9ca0b71eb6196b14f444f7bb9099f436fcc26ce4fac0d27f99e0fdee"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/typstyle")
