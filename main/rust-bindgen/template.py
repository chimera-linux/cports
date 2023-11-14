pkgname = "rust-bindgen"
pkgver = "0.69.1"
pkgrel = 0
build_style = "cargo"
make_build_args = ["--bins"]
make_install_args = ["--bins"]
hostmakedepends = ["cargo"]
makedepends = ["rust-std"]
depends = ["libclang"]
checkdepends = ["libclang"]
pkgdesc = "Tool to generate Rust bindings for C/C++ code"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://rust-lang.github.io/rust-bindgen"
source = (
    f"https://github.com/rust-lang/{pkgname}/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "c10e2806786fb75f05ef32f3f03f4cb7e37bb8e06be5a4a0e95f974fdc567d87"
# needs rustfmt nightly to run suite
options = ["!check"]


def do_install(self):
    self.cargo.install(wrksrc="bindgen-cli")
    self.install_license("LICENSE")
