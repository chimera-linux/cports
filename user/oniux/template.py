pkgname = "oniux"
pkgver = "0.13.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "cmake", "pkgconf", "rust-bindgen"]
makedepends = ["openssl3-devel", "rust-std", "sqlite-devel", "zstd-devel"]
pkgdesc = "Kernel-level Tor isolation for Linux applications"
license = "MIT OR Apache-2.0"
url = "https://gitlab.torproject.org/tpo/core/oniux"
source = f"{url}/-/archive/v{pkgver}/oniux-v{pkgver}.tar.gz"
sha256 = "a8c182df284eca395bc6d9edd1bf12d8044de7722fa49ff16f92be0bb36b3201"
# no tests
options = ["!check"]

if self.profile.wordsize == 32:
    broken = "atomic64"

if self.profile.endian == "big":
    broken = "merlin crate doesn't support big endian"


def install(self):
    from cbuild.util import cargo

    self.install_bin(cargo.target_path(self, "oniux"))
    self.install_license("LICENSE-MIT")
