pkgname = "amdgpu_top"
pkgver = "0.9.2"
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
sha256 = "df447ff5cb4bd3ba70e80b6c180eb4f7b5b6aefc23a0436b194c3edc55c43e81"
# no tests
options = ["!check"]


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/amdgpu_top")
    self.install_file("assets/amdgpu_top.desktop", "usr/share/applications")
    self.install_license("LICENSE")
