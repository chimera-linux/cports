pkgname = "gleam"
pkgver = "1.10.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
checkdepends = ["erlang", "git", "nodejs"]
depends = ["erlang"]
pkgdesc = "Friendly language for building scalable type-safe systems"
license = "Apache-2.0"
url = "https://gleam.run"
source = (
    f"https://github.com/gleam-lang/gleam/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "4661bebc010209c5c3d180a8f7ad6c16b596655acf74bf459d3baf81af8589d5"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/gleam")
