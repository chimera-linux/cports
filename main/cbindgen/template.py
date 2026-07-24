pkgname = "cbindgen"
pkgver = "0.29.4"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Tool to generate C bindings for Rust code"
license = "MPL-2.0"
url = "https://github.com/eqrion/cbindgen"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "9b5757e915cf8be523d3aca282b9b5651bafa112e14bf1ba488562ba282807d6"
# only expected to work with rust nightly
options = ["!check"]


def install(self):
    self.install_bin(f"./target/{self.profile().triplet}/release/cbindgen")
