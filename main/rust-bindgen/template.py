pkgname = "rust-bindgen"
pkgver = "0.72.1"
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
sha256 = "4ffb17061b2d71f19c5062d2e17e64107248f484f9775c0b7d30a16a8238dfd1"
# needs rustfmt nightly to run suite
options = ["!check"]


def install(self):
    self.install_bin(f"./target/{self.profile().triplet}/release/bindgen")
    self.install_license("LICENSE")
