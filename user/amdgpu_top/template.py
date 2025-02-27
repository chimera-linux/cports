pkgname = "amdgpu_top"
pkgver = "0.10.3"
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
sha256 = "b74065ea89fb35a572dddccc22b71e81b7cb1e76b83027704814595e4fcdc6e4"
# no tests
options = ["!check"]


if self.profile().wordsize == 32:
    broken = "64-bit assumptions in libdrm_amdgpu_sys"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/amdgpu_top")
    self.install_file("assets/amdgpu_top.desktop", "usr/share/applications")
    self.install_license("LICENSE")
