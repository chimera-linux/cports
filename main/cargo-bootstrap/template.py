pkgname = "cargo-bootstrap"
pkgver = "1.63.0"
pkgrel = 0
# satisfy runtime dependencies
hostmakedepends = ["curl"]
depends = ["!cargo"]
pkgdesc = "Bootstrap binaries of Rust package manager"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT OR Apache-2.0"
url = "https://rust-lang.org"
source = f"https://repo.chimera-linux.org/distfiles/cargo-{pkgver}-{self.profile().triplet}.tar.xz"
options = ["!strip"]

match self.profile().arch:
    case "aarch64":
        sha256 = "4bb96de4082ea2a0123c0961f12c44ceacd098e7e4cae07faa2a0bb52f725c56"
    case "ppc64le":
        sha256 = "f6893f739872c21d56fc7517911617870f2ebfb6dc6d785cadaffe07c1035415"
    case "x86_64":
        sha256 = "596f930c7225fb48b3d2d916f22cf862869eb1baddcd0a529d4f62f17803be8e"
    case _:
        broken = f"not yet built for {self.profile().arch}"

def do_install(self):
    self.install_bin("cargo")
    self.install_license("LICENSE-APACHE")
    self.install_license("LICENSE-MIT")
    self.install_license("LICENSE-THIRD-PARTY")
