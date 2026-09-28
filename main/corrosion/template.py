pkgname = "corrosion"
pkgver = "0.6.1"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Tool for integrating Rust into an existing CMake project"
license = "MIT"
url = "https://github.com/corrosion-rs/corrosion"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "e9e95b1ee2bad52681f347993fb1a5af5cce458c5ce8a2636c9e476e4babf8e3"
# Checks require rustup, because they support specifying specific toolchains
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
