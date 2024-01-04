pkgname = "cargo-bootstrap"
pkgver = "1.74.0"
pkgrel = 0
# satisfy runtime dependencies
hostmakedepends = ["curl"]
# satisfy revdeps
makedepends = ["zlib"]
depends = ["!cargo"]
pkgdesc = "Bootstrap binaries of Rust package manager"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT OR Apache-2.0"
url = "https://rust-lang.org"
source = f"https://repo.chimera-linux.org/distfiles/cargo-{pkgver}-{self.profile().triplet}.tar.xz"
options = ["!strip"]

match self.profile().arch:
    case "aarch64":
        sha256 = (
            "b6da9f051e568b54d849e8fe664e047d4eb4f5158f845baa45fc085a5725870a"
        )
    case "ppc64le":
        sha256 = (
            "1ef6b68d98f23f9efdc5510db45b4c7391b7acd1fbcd5392e7ac0e573f18ee6e"
        )
    case "ppc64":
        sha256 = (
            "e3d909739c7f3cd37caae0190ac96019345fdf240d8c9e7cbb428ebee5ec8031"
        )
    case "riscv64":
        sha256 = (
            "97f92d93105bf08b329b4700142e189d595ff4a3520fc4432de8f7207f90f4c9"
        )
    case "x86_64":
        sha256 = (
            "7e65b6779d19dd7614a6e431f3445b2cfbdb67d72c9ede00a1fd168d33382f2e"
        )
    case _:
        broken = f"not yet built for {self.profile().arch}"


def do_install(self):
    self.install_bin("cargo")
    self.install_license("LICENSE-MIT")
    self.install_license("LICENSE-THIRD-PARTY")
