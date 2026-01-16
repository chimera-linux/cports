pkgname = "gurk"
pkgver = "0.7.2"
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
source = [
    f"{url}/archive/refs/tags/v{pkgver}.tar.gz",
    "https://github.com/whisperfish/presage/archive/ed011688fc8d9c0ee07c3d44743c138c1fa4dfda.tar.gz",
]
source_paths = [".", "presage"]
sha256 = [
    "1b349555a7fc5bc0e8e5a417b1cc49e4107360e3de6d1eb9cbf8f254bc57f9b8",
    "4e142d8f2bed05d2a085dae24f8b29929a21e0c6fb28d8515e9110a8c5507974",
]


def post_patch(self):
    self.mv("presage/.sqlx", "vendor/presage-store-sqlite")


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/gurk")
    self.install_license("LICENSE-AGPL-3.0")
