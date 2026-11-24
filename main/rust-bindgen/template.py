pkgname = "rust-bindgen"
pkgver = "0.73.2"
pkgrel = 0
build_style = "cargo"
make_build_args = ["--bins"]
make_install_args = ["--bins"]
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
depends = ["clang-libs"]
checkdepends = ["clang-libs"]
pkgdesc = "Tool to generate Rust bindings for C/C++ code"
license = "BSD-3-Clause"
url = "https://rust-lang.github.io/rust-bindgen"
source = f"https://github.com/rust-lang/rust-bindgen/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "5fc3277dd334e4bbbd7bdb8cad5d4fb87a667b2e95a2bae350a8d5424c280629"
# needs rustfmt nightly to run suite
options = ["!check"]


def install(self):
    from cbuild.util import cargo

    self.install_bin(cargo.target_path(self, "bindgen"))
    self.install_license("LICENSE")
