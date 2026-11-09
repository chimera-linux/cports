pkgname = "oniux"
pkgver = "0.15.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "cmake", "pkgconf", "rust-bindgen"]
makedepends = ["openssl3-devel", "rust-std", "sqlite-devel", "zstd-devel"]
pkgdesc = "Kernel-level Tor isolation for Linux applications"
license = "MIT OR Apache-2.0"
url = "https://gitlab.torproject.org/tpo/core/oniux"
source = f"{url}/-/archive/v{pkgver}/oniux-v{pkgver}.tar.gz"
sha256 = "45e72703250168de062d2976fd09b72185c12e64bedae443b06a042b591e9cce"
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
