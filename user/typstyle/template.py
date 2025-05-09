pkgname = "typstyle"
pkgver = "0.13.6"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Typst code formatter"
license = "Apache-2.0"
url = "https://github.com/Enter-tainer/typstyle"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "3ecac7ccd9e8e6d3ac5750b3036dc0253a4a228c9270c14e0a499c6ae677eb42"

if self.profile().wordsize == 32:
    broken = "needs atomic64"

if self.profile().arch in ["loongarch64"]:
    broken = "sigbus in tests"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/typstyle")
