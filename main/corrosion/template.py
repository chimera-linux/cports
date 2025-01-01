pkgname = "corrosion"
pkgver = "0.5.1"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Tool for integrating Rust into an existing CMake project"
maintainer = "Jan Christian Grünhage <jan.christian@gruenhage.xyz>"
license = "MIT"
url = "https://github.com/corrosion-rs/corrosion"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "843334a9f0f5efbc225dccfa88031fe0f2ec6fd787ca1e7d55ed27b2c25d9c97"
# Checks require rustup, because they support specifying specific toolchains
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
