pkgname = "chars"
pkgver = "0.7.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "CLI tool to display information about unicode characters"
license = "MIT"
url = "https://github.com/boinkor-net/chars"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "2f79843a3b1173870b41ebce491a54812b13a44090d0ae30a6f572caa91f0736"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/chars")
    self.install_license("LICENSE")
