pkgname = "typstyle"
pkgver = "0.13.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Typst code formatter"
maintainer = "ttyyls <contact@behri.org>"
license = "Apache-2.0"
url = "https://github.com/Enter-tainer/typstyle"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "2a57d02df94d50e7b0e721ab0d3e6139a1ee892b51a5afb6e1ea8c62f637151f"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/typstyle")
