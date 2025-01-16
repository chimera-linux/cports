pkgname = "cbindgen"
pkgver = "0.28.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Tool to generate C bindings for Rust code"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MPL-2.0"
url = "https://github.com/eqrion/cbindgen"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "b0ed39dda089cafba583e407183e43de151d2ae9d945d74fb4870db7e4ca858e"
# only expected to work with rust nightly
options = ["!check"]


def install(self):
    self.install_bin(f"./target/{self.profile().triplet}/release/cbindgen")
