# Keep in sync with cargo-auditable-bootstrap
pkgname = "cargo-auditable"
pkgver = "0.6.5"
pkgrel = 0
build_style = "cargo"
make_build_args = ["-p", "cargo-auditable"]
make_check_args = [
    *make_build_args,
    "--",
    "--skip",
    # probably fails because we have slightly older cargo
    "test_wasm",
]
hostmakedepends = ["cargo-auditable-bootstrap"]
makedepends = ["rust-std"]
depends = ["cargo"]
pkgdesc = "Tool for embedding dependency information in rust binaries"
maintainer = "Jan Christian Grünhage <jan.christian@gruenhage.xyz>"
license = "Apache-2.0 OR MIT"
url = "https://github.com/rust-secure-code/cargo-auditable"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "5e7dad2d00cba7f09f92f457999d15b7fb786a5ddd1adf87ddbc634878ab5589"


def install(self):
    self.install_bin(
        f"./target/{self.profile().triplet}/release/cargo-auditable"
    )
    self.install_license("LICENSE-MIT")
