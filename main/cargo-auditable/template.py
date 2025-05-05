# Keep in sync with cargo-auditable-bootstrap
pkgname = "cargo-auditable"
pkgver = "0.6.7"
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
sha256 = "07641dab34429b7d31ee29bd4f0b426fa486e0be81fce2234d5936d0ba240ee8"


def install(self):
    self.install_bin(
        f"./target/{self.profile().triplet}/release/cargo-auditable"
    )
    self.install_license("LICENSE-MIT")
