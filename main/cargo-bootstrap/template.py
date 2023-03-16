pkgname = "cargo-bootstrap"
pkgver = "1.68.0"
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
        sha256 = "a8359051529362575b095929fc6d6052fe6f1cfc2973a9d2b76d8a53848b12e3"
    case "ppc64le":
        sha256 = "42f636faa0416aec81e1694c2ed266bed88979c466aab1da899ab5e06fb3e850"
    case "riscv64":
        sha256 = "6188917978f0c58bffb4e1914e0dd1d1ad2b798a34a0ab0cff0087c087504fdf"
    case "x86_64":
        sha256 = "712f4cd05e7b52bee95fd89e18778f2e8a430ad6ccff7d21b6a5376b077efad0"
    case _:
        broken = f"not yet built for {self.profile().arch}"

def do_install(self):
    self.install_bin("cargo")
    self.install_license("LICENSE-APACHE")
    self.install_license("LICENSE-MIT")
    self.install_license("LICENSE-THIRD-PARTY")
