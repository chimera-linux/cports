pkgname = "corrosion"
pkgver = "0.4.8"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "cargo"]
pkgdesc = "Tool for integrating Rust into an existing CMake project"
maintainer = "Jan Christian Grünhage <jan.christian@gruenhage.xyz>"
license = "MIT"
url = "https://github.com/corrosion-rs/corrosion"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "6b9090647d372adec2b09ac7a553458b6e39004238967f9a25e9dd8c1d77584d"
# Checks require rustup, because they support specifying specific toolchains
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
