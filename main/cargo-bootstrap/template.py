pkgname = "cargo-bootstrap"
pkgver = "1.60.0"
pkgrel = 0
# satisfy runtime dependencies
hostmakedepends = ["curl"]
depends = ["!cargo"]
pkgdesc = "Bootstrap binaries of Rust package manager"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT OR Apache-2.0"
url = "https://rust-lang.org"
source = f"https://ftp.octaforge.org/chimera/distfiles/cargo-{pkgver}-{self.profile().triplet}.tar.xz"
options = ["!strip"]

match self.profile().arch:
    case "ppc64le":
        sha256 = "29d19c5015d97c862af365cda33339619fb23ae9a2ae2ea5290765604f99e47d"
    case "x86_64":
        sha256 = "07ab0bdeaf14f31fe07e40f2b3a9a6ae18a4b61579c8b6fa22ecd684054a81af"
    case _:
        broken = f"not yet built for {self.profile().arch}"

def do_install(self):
    self.install_bin("cargo")
    self.install_license("LICENSE-APACHE")
    self.install_license("LICENSE-MIT")
    self.install_license("LICENSE-THIRD-PARTY")
