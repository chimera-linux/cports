pkgname = "rust-bindgen"
pkgver = "0.71.1"
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
sha256 = "620d80c32b6aaf42d12d85de86fc56950c86b2a13a5b943c10c29d30c4f3efb0"
# needs rustfmt nightly to run suite
options = ["!check"]


def install(self):
    self.install_bin(f"./target/{self.profile().triplet}/release/bindgen")
    self.install_license("LICENSE")
