pkgname = "amdgpu_top"
pkgver = "0.8.5"
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
sha256 = "7fe7c64962b56d9da41930a3d0f07910f04ceaebda8143d52da75e2f53aa0032"
# no tests
options = ["!check"]


def do_install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/amdgpu_top")
    self.install_license("LICENSE")
