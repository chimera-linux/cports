pkgname = "cargo-bootstrap"
pkgver = "1.64.0"
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
        sha256 = "72942b54d0fc4191b75da9539ead0a2eba7e11fe9fe8e15e9477168fc0225ccf"
    case "ppc64le":
        sha256 = "c80c1c516fddac73555478d10c3fa2515c0240a000faad00cedae2cf5f185617"
    case "x86_64":
        sha256 = "61de253f797919bd96f01b0e69206ec6b9748557e8907d0333734d8c8338ce74"
    case _:
        broken = f"not yet built for {self.profile().arch}"

def do_install(self):
    self.install_bin("cargo")
    self.install_license("LICENSE-APACHE")
    self.install_license("LICENSE-MIT")
    self.install_license("LICENSE-THIRD-PARTY")
