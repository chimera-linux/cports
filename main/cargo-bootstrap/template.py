pkgname = "cargo-bootstrap"
pkgver = "1.61.0"
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
        sha256 = "8175b74ec0d7d0cc0a60af5b9e4bd30258cca24d597db7f8b88d92fb3c017c20"
    case "x86_64":
        sha256 = "03ffdaab9abd9732d27766a4721320c8e73b7b1a699f7d63cd26cbe7f04d222f"
    case _:
        broken = f"not yet built for {self.profile().arch}"

def do_install(self):
    self.install_bin("cargo")
    self.install_license("LICENSE-APACHE")
    self.install_license("LICENSE-MIT")
    self.install_license("LICENSE-THIRD-PARTY")
