pkgname = "gleam"
pkgver = "1.9.1"
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
sha256 = "eacf88d2ce6f7ca06e9a0d6b8117c517a8a21593349233edb2506263d08a830f"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/gleam")
