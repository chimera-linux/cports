pkgname = "gleam"
pkgver = "1.14.0"
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
sha256 = "2463831e404762b0a759db874907ab475474535ac2e976a9f249196e34ece054"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/gleam")
