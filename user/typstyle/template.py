pkgname = "typstyle"
pkgver = "0.13.13"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Typst code formatter"
license = "Apache-2.0"
url = "https://github.com/Enter-tainer/typstyle"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "19d0d95cbb71cc532530957849aeb85234afeb5e1a8e7fbb7a07bdb23ac260ce"

if self.profile().wordsize == 32:
    broken = "needs atomic64"

if self.profile().arch in ["loongarch64"]:
    broken = "sigbus in tests"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/typstyle")
