pkgname = "rust-bindgen"
pkgver = "0.70.1"
pkgrel = 0
build_style = "cargo"
make_build_args = ["--bins"]
make_install_args = ["--bins"]
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
depends = ["clang-libs"]
checkdepends = ["clang-libs"]
pkgdesc = "Tool to generate Rust bindings for C/C++ code"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://rust-lang.github.io/rust-bindgen"
source = f"https://github.com/rust-lang/rust-bindgen/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "243ed50f99c00ae8c18d50429a1278b6fd37dff94df46df38f2733745362c014"
# needs rustfmt nightly to run suite
options = ["!check"]


def install(self):
    self.install_bin(f"./target/{self.profile().triplet}/release/bindgen")
    self.install_license("LICENSE")
