pkgname = "amdgpu_top"
pkgver = "0.11.0"
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
sha256 = "a56152d738a0bfc3757d9587aaed409ecb05ccc3ec81861cbc9e4af84aa9fd46"
# no tests
options = ["!check"]


if self.profile().wordsize == 32:
    broken = "64-bit assumptions in libdrm_amdgpu_sys"


def pre_prepare(self):
    # rustix loongarch64
    self.do(
        "cargo",
        "update",
        "--package",
        "libc",
        "--precise",
        "0.2.174",
        allow_network=True,
    )


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/amdgpu_top")
    self.install_file("assets/amdgpu_top.desktop", "usr/share/applications")
    self.install_license("LICENSE")
