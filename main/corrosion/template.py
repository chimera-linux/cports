pkgname = "corrosion"
pkgver = "0.5.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Tool for integrating Rust into an existing CMake project"
maintainer = "Jan Christian Grünhage <jan.christian@gruenhage.xyz>"
license = "MIT"
url = "https://github.com/corrosion-rs/corrosion"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "bbe0d4a31cef91b890134af82789fb6e8ecc33270472beea9cecb8f2b7b7ed65"
# Checks require rustup, because they support specifying specific toolchains
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
