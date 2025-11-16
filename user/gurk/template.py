pkgname = "gurk"
pkgver = "0.8.1"
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
sha256 = "08077c44f4cee3b5f2f31a0cc90d978e052a51677ed73af61419093ca154163f"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/gurk")
    self.install_license("LICENSE-AGPL-3.0")
