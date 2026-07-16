pkgname = "gurk"
pkgver = "0.9.3"
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
sha256 = "1c8ee4466374375a3df2ccd94fcc86d76bfcdd868820f3f9d4a1f2cbed2be22b"


def post_patch(self):
    from cbuild.util import cargo

    cargo.clear_vendor_checksums(self, "libc-0.2.180")


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/gurk")
    self.install_license("LICENSE-AGPL-3.0")
