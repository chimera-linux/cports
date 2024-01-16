pkgname = "rust-bindgen"
pkgver = "0.69.2"
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
source = f"https://github.com/rust-lang/rust-bindgen/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "78fbb8bd100e145d1effc982eaab21b555ccc3fc1cbe6e734f17cdfe5c33af32"
# needs rustfmt nightly to run suite
options = ["!check"]


def do_install(self):
    self.cargo.install(wrksrc="bindgen-cli")
    self.install_license("LICENSE")
