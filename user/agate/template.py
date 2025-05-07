pkgname = "agate"
pkgver = "3.3.16"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["rust-std"]
checkdepends = ["openssl3-devel"]
pkgdesc = "Server for the Gemini Protocol"
license = "Apache-2.0 OR MIT"
url = "https://github.com/mbrubeck/agate"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "943a77d2416871b663264e079925806afd3b1109df43523b6da8f60e89afa27b"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/agate")
    self.install_license("LICENSE-MIT")
