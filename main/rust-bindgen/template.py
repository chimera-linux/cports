pkgname = "rust-bindgen"
pkgver = "0.64.0"
pkgrel = 0
build_style = "cargo"
make_build_args = ["--bins"]
make_install_args = ["--bins", "--path", "bindgen-cli"]
hostmakedepends = ["cargo"]
makedepends = ["rust"]
depends = ["libclang"]
checkdepends = ["libclang"]
pkgdesc = "Tool to generate Rust bindings for C/C++ code"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://rust-lang.github.io/rust-bindgen"
source = f"https://github.com/rust-lang/{pkgname}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "9d987e7e2cefebed2c856ba36438e75af00aa08d4274fc15b8c20886065cb1f2"
# needs rustfmt nightly to run suite
options = ["!check"]

def post_install(self):
    self.install_license("LICENSE")
