pkgname = "rust-bindgen"
pkgver = "0.69.4"
pkgrel = 2
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
sha256 = "c02ce18b95c4e5021b95b8b461e5dbe6178edffc52a5f555cbca35b910559b5e"
# needs rustfmt nightly to run suite
options = ["!check"]


def do_install(self):
    self.install_bin(f"./target/{self.profile().triplet}/release/bindgen")
    self.install_license("LICENSE")
