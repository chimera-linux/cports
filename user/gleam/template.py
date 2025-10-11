pkgname = "gleam"
pkgver = "1.12.0"
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
sha256 = "5ea236d1eacbdf06922f99fc2c06acb0fb50c7dae713ac3106b9fabd51744a7c"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/gleam")
