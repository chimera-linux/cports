# Keep in sync with cargo-auditable-bootstrap
pkgname = "cargo-auditable"
pkgver = "0.7.0"
pkgrel = 0
build_style = "cargo"
make_build_args = ["-p", "cargo-auditable"]
make_check_args = [
    *make_build_args,
    "--",
    "--skip=test_self_hosting",
    "--skip=test_wasm",
]
hostmakedepends = ["cargo-auditable-bootstrap"]
makedepends = ["rust-std", "rust-wasm"]
depends = ["cargo"]
pkgdesc = "Tool for embedding dependency information in rust binaries"
license = "Apache-2.0 OR MIT"
url = "https://github.com/rust-secure-code/cargo-auditable"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "d2b81a7da3cb6c03d8cd977c36dc9adf7f2a3a587ce7c35c8e97ced5a9c83334"


def install(self):
    self.install_bin(
        f"./target/{self.profile().triplet}/release/cargo-auditable"
    )
    self.install_license("LICENSE-MIT")
