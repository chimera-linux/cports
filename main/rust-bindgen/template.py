pkgname = "rust-bindgen"
pkgver = "0.66.1"
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
source = (
    f"https://github.com/rust-lang/{pkgname}/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "adedec96f2a00ce835a7c31656e09d6aae6ef55df9ca3d8d65d995f8f2542388"
# needs rustfmt nightly to run suite
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
