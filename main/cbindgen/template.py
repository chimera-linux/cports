pkgname = "cbindgen"
pkgver = "0.29.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Tool to generate C bindings for Rust code"
license = "MPL-2.0"
url = "https://github.com/eqrion/cbindgen"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "6697f449d4a15d814d991249a611af961c97e36d9344c7ced6df35c5c25b40cc"
# only expected to work with rust nightly
options = ["!check"]


def install(self):
    self.install_bin(f"./target/{self.profile().triplet}/release/cbindgen")
