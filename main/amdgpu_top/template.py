pkgname = "amdgpu_top"
pkgver = "0.10.0"
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
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "MIT"
url = "https://github.com/Umio-Yasuno/amdgpu_top"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "116020dcd15d0390ed55a0dffea6e110e658926d6bfa444bf1c23edc2cb794ad"
# no tests
options = ["!check"]


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/amdgpu_top")
    self.install_file("assets/amdgpu_top.desktop", "usr/share/applications")
    self.install_license("LICENSE")
