pkgname = "typstyle"
pkgver = "0.13.11"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Typst code formatter"
license = "Apache-2.0"
url = "https://github.com/Enter-tainer/typstyle"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "7a7bff0980f00f468dfadc04e2c26531ea7d2301b2909bf2cb24116c97902ec7"

if self.profile().wordsize == 32:
    broken = "needs atomic64"

if self.profile().arch in ["loongarch64"]:
    broken = "sigbus in tests"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/typstyle")
