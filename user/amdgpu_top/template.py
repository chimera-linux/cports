pkgname = "amdgpu_top"
pkgver = "0.11.5"
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
license = "MIT"
url = "https://github.com/Umio-Yasuno/amdgpu_top"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "e511ed15a6e0f3ea72321dfc97145ffb85999b37b6b304e9795978945f3f04cd"
# no tests
options = ["!check"]


if self.profile().wordsize == 32:
    broken = "64-bit assumptions in libdrm_amdgpu_sys"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/amdgpu_top")
    self.install_file("assets/amdgpu_top.desktop", "usr/share/applications")
    self.install_license("LICENSE")
