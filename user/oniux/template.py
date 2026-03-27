pkgname = "oniux"
pkgver = "0.7.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "cmake", "pkgconf", "rust-bindgen"]
makedepends = ["openssl3-devel", "rust-std", "sqlite-devel", "zstd-devel"]
pkgdesc = "Kernel-level Tor isolation for Linux applications"
license = "MIT OR Apache-2.0"
url = "https://gitlab.torproject.org/tpo/core/oniux"
source = f"{url}/-/archive/v{pkgver}/oniux-v{pkgver}.tar.gz"
sha256 = "e84e9237e16b6f119ef2c02c05f94161fdd903727f9bf6038ccd2418228e8473"
# no tests
options = ["!check"]


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/oniux")
    self.install_license("LICENSE-MIT")
