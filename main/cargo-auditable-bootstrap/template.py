# Keep in sync with cargo-auditable
pkgname = "cargo-auditable-bootstrap"
pkgver = "0.7.1"
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
license = "Apache-2.0 OR MIT"
url = "https://github.com/rust-secure-code/cargo-auditable"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "e79d1daba3d9a6fc37193d67c9442bd8f90c228c27ead1f21fb6e51630917527"


def install(self):
    self.install_bin(
        f"./target/{self.profile().triplet}/release/cargo-auditable"
    )
    self.install_license("LICENSE-MIT")
