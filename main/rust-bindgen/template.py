pkgname = "rust-bindgen"
pkgver = "0.68.1"
pkgrel = 0
build_style = "cargo"
make_build_args = ["--bins"]
make_install_args = ["--bins"]
hostmakedepends = ["cargo"]
makedepends = ["rust"]
depends = ["libclang"]
checkdepends = ["libclang"]
pkgdesc = "Tool to generate Rust bindings for C/C++ code"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://rust-lang.github.io/rust-bindgen"
source = (
    f"https://github.com/rust-lang/{pkgname}/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "6a577026184a6f7a99b48f46f2074c83d272d3aadf91c7b94a4c6c34e6acd445"
# needs rustfmt nightly to run suite
options = ["!check"]


def do_install(self):
    self.cargo.install(wrksrc="bindgen-cli")
    self.install_license("LICENSE")
