pkgname = "gurk"
pkgver = "0.10.2"
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
sha256 = "d047915916bceb221cd96a8afe53e5ba3b897f8d8798a4d36ca4cf354aa63b03"


def install(self):
    from cbuild.util import cargo

    self.install_bin(cargo.target_path(self, "gurk"))
    self.install_license("LICENSE-AGPL-3.0")
