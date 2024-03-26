pkgname = "corrosion"
pkgver = "0.4.7"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "cargo"]
pkgdesc = "Tool for integrating Rust into an existing CMake project"
maintainer = "Jan Christian Grünhage <jan.christian@gruenhage.xyz>"
license = "MIT"
url = "https://github.com/corrosion-rs/corrosion"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "f1fbb39e627e1972a5922895548e4fecaec39a06a538a1d26225d95c219a163e"
# Checks require rustup, because they support specifying specific toolchains
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
