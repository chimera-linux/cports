pkgname = "cbindgen"
pkgver = "0.29.2"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Tool to generate C bindings for Rust code"
license = "MPL-2.0"
url = "https://github.com/eqrion/cbindgen"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "c7d4d610482390c70e471a5682de714967e187ed2f92f2237c317a484a8c7e3a"
# only expected to work with rust nightly
options = ["!check"]


def install(self):
    self.install_bin(f"./target/{self.profile().triplet}/release/cbindgen")
