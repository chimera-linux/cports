pkgname = "cbindgen"
pkgver = "0.26.0"
pkgrel = 1
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Tool to generate C bindings for Rust code"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MPL-2.0"
url = "https://github.com/eqrion/cbindgen"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "b45e1a64875b615702a86ac3084ef69ae32926241cd2b687a30c12474be15105"
# only expected to work with rust nightly
options = ["!check"]


def do_install(self):
    self.install_bin(f"./target/{self.profile().triplet}/release/cbindgen")
