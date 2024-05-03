pkgname = "corrosion"
pkgver = "0.4.9"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "cargo"]
pkgdesc = "Tool for integrating Rust into an existing CMake project"
maintainer = "Jan Christian Grünhage <jan.christian@gruenhage.xyz>"
license = "MIT"
url = "https://github.com/corrosion-rs/corrosion"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "3346b21c4986c077988e10a19b8737a7b56f6f84ef8e800058b58d1f138e8fa9"
# Checks require rustup, because they support specifying specific toolchains
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
