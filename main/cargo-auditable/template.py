# Keep in sync with cargo-auditable-bootstrap
pkgname = "cargo-auditable"
pkgver = "0.6.4"
pkgrel = 1
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
sha256 = "3e3f4134d81b47277d34c44bc1169c9b0356612977651f8e98e2ba1a470b69a2"


def install(self):
    self.install_bin(
        f"./target/{self.profile().triplet}/release/cargo-auditable"
    )
    self.install_license("LICENSE-MIT")
