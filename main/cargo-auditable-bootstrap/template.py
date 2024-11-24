# Keep in sync with cargo-auditable
pkgname = "cargo-auditable-bootstrap"
pkgver = "0.6.6"
pkgrel = 0
build_style = "cargo"
make_build_args = ["-p", "cargo-auditable"]
make_check_args = [
    *make_build_args,
    "--",
    "--skip=test_self_hosting",
    "--skip=test_wasm",
]
hostmakedepends = ["cargo"]
makedepends = ["rust-std"]
depends = ["cargo"]
pkgdesc = "Tool for embedding dependency information in rust binaries"
maintainer = "Jan Christian Grünhage <jan.christian@gruenhage.xyz>"
license = "Apache-2.0 OR MIT"
url = "https://github.com/rust-secure-code/cargo-auditable"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "adecc1ccf8e86f4e3734767ee6a1c90e04c6639a4f73a59ac2db68a07220c807"


def install(self):
    self.install_bin(
        f"./target/{self.profile().triplet}/release/cargo-auditable"
    )
    self.install_license("LICENSE-MIT")
