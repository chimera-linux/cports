pkgname = "oniux"
pkgver = "0.11.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "cmake", "pkgconf", "rust-bindgen"]
makedepends = ["openssl3-devel", "rust-std", "sqlite-devel", "zstd-devel"]
pkgdesc = "Kernel-level Tor isolation for Linux applications"
license = "MIT OR Apache-2.0"
url = "https://gitlab.torproject.org/tpo/core/oniux"
source = f"{url}/-/archive/v{pkgver}/oniux-v{pkgver}.tar.gz"
sha256 = "ea59ce1f2884c1cbdcd981fbdef06e7f3a6f12d25870dbd8cc8a213ea80737a8"
# no tests
options = ["!check"]

if self.profile().wordsize == 32:
    broken = "atomic64"

if self.profile().endian == "big":
    broken = "merlin crate doesn't support big endian"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/oniux")
    self.install_license("LICENSE-MIT")
