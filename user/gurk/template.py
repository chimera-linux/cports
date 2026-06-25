pkgname = "gurk"
pkgver = "0.9.1"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf", "protobuf-protoc"]
makedepends = [
    "openssl3-devel",
    "protobuf-devel",
    "rust-std",
    "sqlcipher-devel",
    "sqlite-devel",
]
pkgdesc = "Signal Messenger client TUI"
license = "AGPL-3.0-only"
url = "https://github.com/boxdot/gurk-rs"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "7947407eb548bb660227eb03987f7214a48bc92ce48e65ff88cf89ac94461a34"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/gurk")
    self.install_license("LICENSE-AGPL-3.0")
