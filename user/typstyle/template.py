pkgname = "typstyle"
pkgver = "0.13.7"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Typst code formatter"
license = "Apache-2.0"
url = "https://github.com/Enter-tainer/typstyle"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "594e5f65d458250422b4eb05ad66dfbaaa377df97ed88a43f7bd0530c8de4ed2"

if self.profile().wordsize == 32:
    broken = "needs atomic64"

if self.profile().arch in ["loongarch64"]:
    broken = "sigbus in tests"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/typstyle")
