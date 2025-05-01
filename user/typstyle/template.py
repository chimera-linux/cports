pkgname = "typstyle"
pkgver = "0.13.4"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Typst code formatter"
license = "Apache-2.0"
url = "https://github.com/Enter-tainer/typstyle"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "acdee42ef6794050cd08eb658b450712be7b678295267a1d9a990eb0ccd9eb79"

if self.profile().wordsize == 32:
    broken = "needs atomic64"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/typstyle")
