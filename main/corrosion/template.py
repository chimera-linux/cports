pkgname = "corrosion"
pkgver = "0.5.2"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Tool for integrating Rust into an existing CMake project"
license = "MIT"
url = "https://github.com/corrosion-rs/corrosion"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "6bc02411e29183a896aa60c58db6819ec6cf57c08997481d0b0da9029356b529"
# Checks require rustup, because they support specifying specific toolchains
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
