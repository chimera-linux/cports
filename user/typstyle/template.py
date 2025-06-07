pkgname = "typstyle"
pkgver = "0.13.10"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Typst code formatter"
license = "Apache-2.0"
url = "https://github.com/Enter-tainer/typstyle"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "9fe4f555cd3d838341443d92d18d45394d57df08aaab276bbab074ccb1a0fcb3"

if self.profile().wordsize == 32:
    broken = "needs atomic64"

if self.profile().arch in ["loongarch64"]:
    broken = "sigbus in tests"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/typstyle")
