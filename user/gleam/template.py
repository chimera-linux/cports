pkgname = "gleam"
pkgver = "1.13.0"
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
sha256 = "d965a02c1c3b35c70fda49d483eb1fe3fb02045b6126453a1e8e9d91ed029cb4"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/gleam")
