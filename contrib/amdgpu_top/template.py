pkgname = "amdgpu_top"
pkgver = "0.9.0"
pkgrel = 0
build_style = "cargo"
make_build_args = ["--no-default-features", "--features=package"]
hostmakedepends = [
    "cargo-auditable",
    "pkgconf",
]
makedepends = [
    "libdrm-devel",
    "rust-std",
]
pkgdesc = "AMDGPU usage monitor"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://github.com/Umio-Yasuno/amdgpu_top"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "5eb1d51f137fd9488bf83505d83380957c6321dacda014cd826a72313a13ac1d"
# no tests
options = ["!check"]


def do_install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/amdgpu_top")
    self.install_file("assets/amdgpu_top.desktop", "usr/share/applications")
    self.install_license("LICENSE")
