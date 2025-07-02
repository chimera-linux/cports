pkgname = "gleam"
pkgver = "1.11.1"
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
sha256 = "34dfdc397835849bc56ac01bf45e68ee9cfc3c99609fb7b3ab02910930a8c40d"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/gleam")
