pkgname = "cbindgen"
pkgver = "0.27.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Tool to generate C bindings for Rust code"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MPL-2.0"
url = "https://github.com/eqrion/cbindgen"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "af74dd0452ace58895088048873a765fffacc3ad55eea00c0f2999cc4bcf9b5d"
# only expected to work with rust nightly
options = ["!check"]


def install(self):
    self.install_bin(f"./target/{self.profile().triplet}/release/cbindgen")
